"""WebSocket API for Casa Dashboard Community entity configuration."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import voluptuous as vol

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback

from .const import DOMAIN

ENTITY_CONFIG_FILENAME = "casa-dashboard-community-entities.json"
WS_GET = f"{DOMAIN}/config/get"
WS_SAVE = f"{DOMAIN}/config/save"


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
    return {
        "entities": merged,
        "configured": sum(1 for value in merged.values() if value.strip()),
        "total": len(merged),
    }


def _save_config(hass: HomeAssistant, supplied: dict[str, Any]) -> dict[str, Any]:
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
    for meta_key in ("_description", "_author", "_support"):
        if meta_key not in output and meta_key in template:
            output[meta_key] = template[meta_key]

    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(target.suffix + ".tmp")
    temp.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(target)

    return {
        "entities": {key: current_entities.get(key, "") for key in valid},
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
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_save_config(hass: HomeAssistant, connection, msg: dict[str, Any]) -> None:
    """Save the Community entity mapping."""
    result = await hass.async_add_executor_job(_save_config, hass, msg["entities"])
    connection.send_result(msg["id"], result)


@callback
def async_register_websocket_commands(hass: HomeAssistant) -> None:
    """Register Community WebSocket commands."""
    websocket_api.async_register_command(hass, websocket_get_config)
    websocket_api.async_register_command(hass, websocket_save_config)
