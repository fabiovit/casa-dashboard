"""WebSocket API for Casa Dashboard Community entity configuration."""

from __future__ import annotations

import base64
import binascii
import json
import uuid
from pathlib import Path
from typing import Any

import voluptuous as vol

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback

from .const import DOMAIN

ENTITY_CONFIG_FILENAME = "casa-dashboard-community-entities.json"
WS_GET = f"{DOMAIN}/config/get"
WS_SAVE = f"{DOMAIN}/config/save"
WS_UPLOAD_IMAGE = f"{DOMAIN}/config/upload_image"


def _paths(hass: HomeAssistant) -> tuple[Path, Path]:
    target = Path(hass.config.path("www", ENTITY_CONFIG_FILENAME))
    template = Path(__file__).parent / "casa-dashboard-community-entities.example.json"
    return target, template


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _read_config(hass: HomeAssistant) -> dict[str, Any]:
    target, template_path = _paths(hass)
    template = _read_json(template_path)
    current = _read_json(target)

    valid = template.get("entities", {})
    if not isinstance(valid, dict):
        valid = {}
    entities = current.get("entities", {})
    if not isinstance(entities, dict):
        entities = {}

    merged = {
        key: value if isinstance((value := entities.get(key, "")), str) else ""
        for key in valid
    }
    labels = current.get("labels", {})
    if not isinstance(labels, dict):
        labels = {}
    clean_labels = {
        key: str(labels.get(key, "")).strip()
        for key in valid
        if str(labels.get(key, "")).strip()
    }

    rooms = current.get("rooms", [])
    if not isinstance(rooms, list):
        rooms = []

    overview = current.get("overview", {})
    if not isinstance(overview, dict):
        overview = {}
    clean_overview = {
        str(key).strip(): str(value).strip()
        for key, value in overview.items()
        if str(key).strip() and isinstance(value, str) and value.strip()
    }

    return {
        "entities": merged,
        "labels": clean_labels,
        "rooms": rooms,
        "overview": clean_overview,
        "configured": sum(1 for value in merged.values() if value.strip()),
        "total": len(merged),
    }


def _save_config(
    hass: HomeAssistant,
    supplied: dict[str, Any],
    supplied_rooms: list[Any] | None = None,
    supplied_labels: dict[str, Any] | None = None,
    supplied_overview: dict[str, Any] | None = None,
) -> dict[str, Any]:
    target, template_path = _paths(hass)
    template = _read_json(template_path)
    valid = template.get("entities", {})
    if not isinstance(valid, dict):
        valid = {}

    current = _read_json(target)
    output: dict[str, Any] = current if current else dict(template)
    current_entities = output.get("entities")
    if not isinstance(current_entities, dict):
        current_entities = {}

    for key in valid:
        value = supplied.get(key, current_entities.get(key, ""))
        current_entities[key] = value.strip() if isinstance(value, str) else ""

    output["entities"] = current_entities

    current_labels = output.get("labels")
    if not isinstance(current_labels, dict):
        current_labels = {}
    if supplied_labels is not None:
        clean_global_labels: dict[str, str] = {}
        for key in valid:
            label = supplied_labels.get(key, "")
            if isinstance(label, str) and label.strip():
                clean_global_labels[key] = label.strip()
        current_labels = clean_global_labels
    else:
        current_labels = {
            key: str(current_labels.get(key, "")).strip()
            for key in valid
            if str(current_labels.get(key, "")).strip()
        }
    output["labels"] = current_labels

    if supplied_rooms is not None:
        clean_rooms = []
        for room in supplied_rooms:
            if not isinstance(room, dict):
                continue
            rid = str(room.get("id", "")).strip()
            name = str(room.get("name", "")).strip()
            if not rid or not name:
                continue
            entities = room.get("entities", [])
            labels = room.get("entity_labels", {})
            if not isinstance(labels, dict):
                labels = {}
            images = room.get("entity_images", {})
            if not isinstance(images, dict):
                images = {}
            icons = room.get("entity_icons", {})
            if not isinstance(icons, dict):
                icons = {}
            sizes = room.get("entity_sizes", {})
            if not isinstance(sizes, dict):
                sizes = {}
            modules = room.get("modules", [])
            if not isinstance(modules, list):
                modules = []
            clean_modules = [
                str(v).strip()
                for v in modules
                if str(v).strip() in {"solar", "mobility", "weather", "alarm"}
            ]
            clean_entities = [str(x).strip() for x in entities if str(x).strip()] if isinstance(entities, list) else []
            clean_labels = {
                str(k).strip(): str(v).strip()
                for k, v in labels.items()
                if str(k).strip() in clean_entities and str(v).strip()
            }
            clean_entity_images = {
                str(k).strip(): str(v).strip()
                for k, v in images.items()
                if str(k).strip() in clean_entities and str(v).strip()
            }
            clean_entity_icons = {
                str(k).strip(): str(v).strip()
                for k, v in icons.items()
                if str(k).strip() in clean_entities and str(v).strip()
            }
            clean_entity_sizes = {
                str(k).strip(): str(v).strip().lower()
                for k, v in sizes.items()
                if str(k).strip() in clean_entities and str(v).strip().lower() in {"compact", "normal", "wide", "full"}
            }
            clean_rooms.append({
                "id": rid,
                "name": name,
                "type": str(room.get("type", "generico")).strip() or "generico",
                "icon": str(room.get("icon", "mdi:home-outline")).strip() or "mdi:home-outline",
                "image": str(room.get("image", "")).strip(),
                "background_mode": str(room.get("background_mode", "auto")).strip() or "auto",
                "background_value": str(room.get("background_value", "")).strip(),
                "entities": clean_entities,
                "entity_labels": clean_labels,
                "entity_images": clean_entity_images,
                "entity_icons": clean_entity_icons,
                "entity_sizes": clean_entity_sizes,
                "modules": clean_modules,
            })
        output["rooms"] = clean_rooms

    if supplied_overview is not None:
        output["overview"] = {
            str(key).strip(): str(value).strip()
            for key, value in supplied_overview.items()
            if str(key).strip() and isinstance(value, str) and value.strip()
        }
    elif not isinstance(output.get("overview"), dict):
        output["overview"] = {}

    for meta_key in ("_description", "_author", "_support"):
        if meta_key not in output and meta_key in template:
            output[meta_key] = template[meta_key]

    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(target.suffix + ".tmp")
    temp.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(target)

    return {
        "entities": {key: current_entities.get(key, "") for key in valid},
        "labels": {key: current_labels.get(key, "") for key in valid if current_labels.get(key, "")},
        "rooms": output.get("rooms", []),
        "overview": output.get("overview", {}),
        "configured": sum(
            1 for key in valid if isinstance(current_entities.get(key), str) and current_entities[key].strip()
        ),
        "total": len(valid),
    }


@websocket_api.websocket_command({vol.Required("type"): WS_GET})
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_get_config(hass: HomeAssistant, connection, msg: dict[str, Any]) -> None:
    """Return the Community entity mapping."""
    result = await hass.async_add_executor_job(_read_config, hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command(
    {
        vol.Required("type"): WS_SAVE,
        vol.Required("entities"): dict,
        vol.Optional("rooms", default=[]): list,
        vol.Optional("labels", default={}): dict,
        vol.Optional("overview", default={}): dict,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_save_config(hass: HomeAssistant, connection, msg: dict[str, Any]) -> None:
    """Save the Community entity mapping."""
    result = await hass.async_add_executor_job(
        _save_config,
        hass,
        msg["entities"],
        msg.get("rooms", []),
        msg.get("labels", {}),
        msg.get("overview", {}),
    )
    connection.send_result(msg["id"], result)


def _save_uploaded_image(hass: HomeAssistant, data_url: str) -> dict[str, str]:
    """Decode and store a dashboard image under /config/www."""
    if not isinstance(data_url, str) or "," not in data_url:
        raise ValueError("Invalid image payload")
    header, encoded = data_url.split(",", 1)
    mime_map = {
        "data:image/jpeg;base64": ".jpg",
        "data:image/png;base64": ".png",
        "data:image/webp;base64": ".webp",
    }
    extension = mime_map.get(header.lower())
    if not extension:
        raise ValueError("Unsupported image format")
    if len(encoded) > 1_600_000:
        raise ValueError("Image payload is too large")
    try:
        content = base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as err:
        raise ValueError("Invalid image data") from err
    if not content or len(content) > 1_200_000:
        raise ValueError("Image is too large")
    directory = Path(hass.config.path("www", "casa_dashboard_community", "uploads"))
    directory.mkdir(parents=True, exist_ok=True)
    filename = f"{uuid.uuid4().hex}{extension}"
    target = directory / filename
    try:
        target.write_bytes(content)
    except OSError as err:
        raise ValueError(f"Unable to save image: {err}") from err
    if not target.exists() or target.stat().st_size != len(content):
        raise ValueError("Image file could not be verified after saving")
    return {
        "url": f"/local/casa_dashboard_community/uploads/{filename}",
        "size": str(len(content)),
    }


@websocket_api.websocket_command(
    {
        vol.Required("type"): WS_UPLOAD_IMAGE,
        vol.Required("image"): str,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_upload_image(hass: HomeAssistant, connection, msg: dict[str, Any]) -> None:
    """Upload a resized custom room/device image."""
    try:
        result = await hass.async_add_executor_job(_save_uploaded_image, hass, msg["image"])
    except ValueError as err:
        connection.send_error(msg["id"], "invalid_image", str(err))
        return
    connection.send_result(msg["id"], result)


@callback
def async_register_websocket_commands(hass: HomeAssistant) -> None:
    """Register Community WebSocket commands."""
    websocket_api.async_register_command(hass, websocket_get_config)
    websocket_api.async_register_command(hass, websocket_save_config)
    websocket_api.async_register_command(hass, websocket_upload_image)
