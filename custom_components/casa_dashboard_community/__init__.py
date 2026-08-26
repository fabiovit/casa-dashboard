from __future__ import annotations

import inspect
import json
from pathlib import Path

from homeassistant.components import frontend, panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, PANEL_ICON, PANEL_PATH, PANEL_TITLE, STATIC_URL
from .websocket_api import async_register_websocket_commands

VERSION = "3.0.1"
ENTITY_CONFIG_FILENAME = "casa-dashboard-community-entities.json"

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)


def _ensure_entity_config(hass: HomeAssistant) -> None:
    """Create or extend the external entity map without overwriting user values."""
    target = Path(hass.config.path("www", ENTITY_CONFIG_FILENAME))
    source = Path(__file__).parent / "casa-dashboard-community-entities.example.json"

    try:
        template = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return

    target.parent.mkdir(parents=True, exist_ok=True)

    if not target.exists():
        target.write_text(
            json.dumps(template, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return

    # Never replace a malformed/custom file automatically.
    try:
        current = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return

    current_entities = current.get("entities")
    template_entities = template.get("entities")
    if not isinstance(current_entities, dict) or not isinstance(template_entities, dict):
        return

    changed = False
    for key, default_value in template_entities.items():
        if key not in current_entities:
            current_entities[key] = default_value
            changed = True

    for meta_key in ("_description", "_author", "_support"):
        if meta_key not in current and meta_key in template:
            current[meta_key] = template[meta_key]
            changed = True

    if changed:
        temp = target.with_suffix(target.suffix + ".tmp")
        temp.write_text(
            json.dumps(current, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temp.replace(target)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    data = hass.data.setdefault(DOMAIN, {})
    if not data.get("websocket_registered"):
        async_register_websocket_commands(hass)
        data["websocket_registered"] = True
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    data = hass.data.setdefault(DOMAIN, {})

    await hass.async_add_executor_job(_ensure_entity_config, hass)

    if not data.get("static_registered"):
        frontend_dir = Path(__file__).parent / "frontend"
        await hass.http.async_register_static_paths([
            StaticPathConfig(STATIC_URL, str(frontend_dir), False)
        ])
        data["static_registered"] = True

    # Home Assistant compatibility: async_panel_exists is not available
    # in every supported frontend version. The registered panels mapping is
    # stable and avoids failing the first config-entry setup.
    if hass.data.get("frontend_panels", {}).get(PANEL_PATH):
        frontend.async_remove_panel(hass, PANEL_PATH)

    kwargs = {
        "frontend_url_path": PANEL_PATH,
        "webcomponent_name": "casa-dashboard-community-panel",
        "sidebar_title": PANEL_TITLE,
        "sidebar_icon": PANEL_ICON,
        "module_url": f"{STATIC_URL}/casa-dashboard-community-panel.js?v={VERSION}",
        "config": {"version": VERSION},
        "require_admin": False,
    }

    # Compatibility with HA builds before/after handle_safe_area was added.
    if "handle_safe_area" in inspect.signature(panel_custom.async_register_panel).parameters:
        kwargs["handle_safe_area"] = True

    await panel_custom.async_register_panel(hass, **kwargs)
    data["entry_id"] = entry.entry_id
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    if hass.data.get("frontend_panels", {}).get(PANEL_PATH):
        frontend.async_remove_panel(hass, PANEL_PATH)
    hass.data.setdefault(DOMAIN, {}).pop("entry_id", None)
    return True
