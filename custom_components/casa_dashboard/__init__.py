from __future__ import annotations

from pathlib import Path
import inspect
import shutil

from homeassistant.components import frontend, panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, PANEL_ICON, PANEL_PATH, PANEL_TITLE, STATIC_URL

VERSION = "1.0.0"
ENTITY_CONFIG_FILENAME = "casa-dashboard-entities.json"

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)


def _ensure_entity_config(hass: HomeAssistant) -> None:
    target = Path(hass.config.path("www", ENTITY_CONFIG_FILENAME))
    if target.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).parent / "casa-dashboard-entities.example.json"
    shutil.copyfile(source, target)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    hass.data.setdefault(DOMAIN, {})
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

    if frontend.async_panel_exists(hass, PANEL_PATH):
        frontend.async_remove_panel(hass, PANEL_PATH)

    kwargs = {
        "frontend_url_path": PANEL_PATH,
        "webcomponent_name": "casa-dashboard-panel",
        "sidebar_title": PANEL_TITLE,
        "sidebar_icon": PANEL_ICON,
        "module_url": f"{STATIC_URL}/casa-dashboard-panel.js?v={VERSION}",
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
    if frontend.async_panel_exists(hass, PANEL_PATH):
        frontend.async_remove_panel(hass, PANEL_PATH)
    hass.data.setdefault(DOMAIN, {}).pop("entry_id", None)
    return True
