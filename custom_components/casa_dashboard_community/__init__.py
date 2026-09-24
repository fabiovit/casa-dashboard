from __future__ import annotations

import inspect
import json
from pathlib import Path

from homeassistant.components import frontend, panel_custom
from homeassistant.components.lovelace import dashboard as lovelace_dashboard
from homeassistant.components.lovelace.const import ConfigNotFound, LOVELACE_DATA
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, PANEL_ICON, PANEL_PATH, PANEL_TITLE, STATIC_URL
from .websocket_api import async_register_websocket_commands

VERSION = "4.4.0"
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


async def _ensure_lovelace_dashboard_registration(hass: HomeAssistant) -> None:
    """Expose the custom panel in Home Assistant's Dashboards registry.

    Home Assistant's default-dashboard picker is backed by the Lovelace
    dashboards registry.  We keep Casa Dashboard Community as a custom panel
    (so its UI remains unchanged), while maintaining a storage-dashboard
    metadata entry at the same URL.  The Lovelace panel registered for that
    metadata is replaced by our custom panel below.
    """
    lovelace_data = hass.data.get(LOVELACE_DATA)
    if lovelace_data is None:
        return

    # Already known to Lovelace (normal path after the first restart).
    if PANEL_PATH in lovelace_data.dashboards:
        return

    dashboards = lovelace_dashboard.DashboardsCollection(hass)
    await dashboards.async_load()

    existing = next(
        (item for item in dashboards.async_items() if item.get("url_path") == PANEL_PATH),
        None,
    )
    if existing is None:
        # The custom panel may already have been registered by an older setup.
        # Temporarily remove it because Lovelace validates URL uniqueness.
        if hass.data.get("frontend_panels", {}).get(PANEL_PATH):
            frontend.async_remove_panel(hass, PANEL_PATH)
        existing = await dashboards.async_create_item(
            {
                "url_path": PANEL_PATH,
                "title": PANEL_TITLE,
                "icon": PANEL_ICON,
                "show_in_sidebar": True,
                "require_admin": False,
            }
        )

    # Mirror the side effect normally performed by Lovelace's own collection
    # listener, so the entry is immediately visible in Settings > Dashboards
    # and in the per-user default-dashboard picker without waiting for reboot.
    store = lovelace_dashboard.LovelaceStorage(hass, existing)
    try:
        await store.async_load(False)
    except ConfigNotFound:
        await store.async_save({"views": []})
    lovelace_data.dashboards[PANEL_PATH] = store


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    data = hass.data.setdefault(DOMAIN, {})
    if not data.get("websocket_registered"):
        async_register_websocket_commands(hass)
        data["websocket_registered"] = True
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    data = hass.data.setdefault(DOMAIN, {})

    # Config-entry installs may reach async_setup_entry directly. Ensure the
    # websocket commands are registered here as well.
    if not data.get("websocket_registered"):
        async_register_websocket_commands(hass)
        data["websocket_registered"] = True

    await hass.async_add_executor_job(_ensure_entity_config, hass)

    # Register Casa Dashboard Community as a real dashboard metadata entry so
    # Home Assistant can offer it in Settings > Dashboards and as default.
    await _ensure_lovelace_dashboard_registration(hass)

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
