# 🏠 Casa Dashboard Community

🇬🇧 **English** | [🇮🇹 Italiano](README.it.md)

[![Release](https://img.shields.io/badge/release-v4.1.2-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Add to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fabiovit&repository=casa-dashboard&category=integration)

Casa Dashboard Community is a complete app-like dashboard for **Home Assistant**, designed to adapt to different homes without relying on traditional Lovelace cards.

**v4.1.2** is a consolidation release: the project has been cleaned up, versioning is now consistent across backend and frontend, and the mature features introduced in the 2.x generation are retained in a cleaner package.

**Created by Fabio Vittori** · [☕ Buy me a coffee](https://ko-fi.com/fabvittori)

## 🖼️ Casa Dashboard Community 4.0

Version 4.0 introduces a refined visual experience across **dark and light themes**, while keeping the same dynamic room architecture.

### Overview

![Casa Dashboard Community 4.0 - Overview dark theme](images/casa-v4-overview-dark.png)

![Casa Dashboard Community 4.0 - Overview light theme](images/casa-v4-overview-light.png)

### Entrance

![Casa Dashboard Community 4.0 - Entrance dark theme](images/casa-v4-ingresso-dark.png)

![Casa Dashboard Community 4.0 - Entrance light theme](images/casa-v4-ingresso-light.png)

### Kitchen

![Casa Dashboard Community 4.0 - Kitchen dark theme](images/casa-v4-cucina-dark.png)

![Casa Dashboard Community 4.0 - Kitchen light theme](images/casa-v4-cucina-light.png)

### Balcony

![Casa Dashboard Community 4.0 - Balcony dark theme](images/casa-v4-balcone-dark.png)

![Casa Dashboard Community 4.0 - Balcony light theme](images/casa-v4-balcone-light.png)

### Garage, EV and Wallbox

![Casa Dashboard Community 4.0 - Garage dark theme](images/casa-v4-garage-dark.png)

![Casa Dashboard Community 4.0 - Garage light theme](images/casa-v4-garage-light.png)

### Configurator

![Casa Dashboard Community 4.0 - Overview configurator](images/casa-v4-config-overview.png)

![Casa Dashboard Community 4.0 - Rooms configurator](images/casa-v4-config-rooms.png)

![Casa Dashboard Community 4.0 - Energy and Mobility configurator](images/casa-v4-config-energy.png)



## 🛡️ Security & Access

Casa V2 dynamic rooms can now recognize `lock.*` and `alarm_control_panel.*` entities.

When configured in a room, Casa Dashboard automatically adds a dedicated **Security & Access** section with lock status, Lock / Unlock controls, alarm state and quick Home / Away / Off actions.

## ☀️ Advanced Energy View

Casa V2 can now switch the Solar section between **Compact** and **Advanced** mode.

Advanced mode provides an adaptive energy showcase with live solar production, optional PV1/PV2 strings, battery SOC and charge/discharge flow, plus Home / Inverter / Battery / Grid nodes.

Grid and battery sign conventions are configurable, so the view can adapt to different inverter integrations.

## 🧭 Paged configurator

The Casa V2 configurator is now split into dedicated pages:

- Overview
- Rooms
- Devices
- Energy & Mobility
- Weather & Security
- Advanced

This keeps normal configuration simple while moving the full 173-mapping list into an advanced page.

## 🎨 Full visual customization

Casa V2 can now personalize the main Overview section labels, vehicle name and Wallbox name.

Rooms can also use a custom photo. Enter a Home Assistant `/local/...` path (for example `/local/casa/kitchen.jpg`) or an image URL. If no image is configured, the normal Casa V2 visual remains active.

## 🏠 Dynamic rooms

Casa V2 lets you:

- create rooms freely;
- rename and reorder them;
- choose room type and icon;
- create multiple rooms of the same type;
- remove unused rooms;
- assign multiple Home Assistant entities to each room.

## ⚙️ Visual configurator

Configuration is handled directly from the dashboard.

Entities can be searched by:

- Home Assistant friendly name;
- `entity_id`;
- custom display name.

The configurator keeps the **173 Community mappings** used by global and specialized functions.

Global mappings can also have a **custom display name** for the Overview. If left empty, Casa Dashboard uses the Home Assistant friendly name and then the Community fallback name.

Large installations are supported with dedicated scrolling for Rooms and the entity mapping list.

## 🧠 Smart device recognition

Casa V2 can choose a suitable icon/visual using:

1. custom display name;
2. Home Assistant friendly name;
3. recognized function;
4. Home Assistant icon;
5. `device_class`;
6. entity domain.

This helps generic smart plugs appear as the device they actually control when the Home Assistant name provides enough context.

## 📊 V2 Overview

The Overview focuses on useful information rather than duplicating every room:

- active states;
- temperatures;
- outdoor and weather conditions;
- solar production and battery;
- grid data;
- Wallbox and EV.

Unconfigured sections remain hidden.

## 🌍 Languages

Native interface support:

- 🇬🇧 English
- 🇮🇹 Italiano

The language selector is available in the dashboard and the selected language is stored locally.

Custom room names and Home Assistant entity names are preserved.


Individual V2 entities can also use a custom photo. Use **Carica** in the room configurator for lights, switches, appliances, sensors and other objects. Uploaded photos are resized and stored under `/local/casa_dashboard_community/uploads/`; if no photo is set, the normal automatic V2 visual remains active.

## 📱 Responsive

Casa V1 and Casa V2 are designed for desktop and mobile.

## 📦 HACS installation

1. Open **HACS**.
2. Add `https://github.com/fabiovit/casa-dashboard` as a custom repository of type **Integration**, or use the **Add to HACS** button above.
3. Install **Casa Dashboard Community**.
4. Restart Home Assistant.
5. Go to **Settings → Devices & services → Add integration**.
6. Search for **Casa Dashboard Community**.
7. Open the new sidebar panel and press **Configure**.

## 📦 Manual installation

Copy `custom_components/casa_dashboard_community` into `/config/custom_components/`, restart Home Assistant and add the integration from **Settings → Devices & services**.

## ℹ️ Notes

Casa Dashboard Community is an advanced template. Devices, sensors, automations, solar, EV and Wallbox are optional.

Functions that are not configured are hidden automatically.

## ☕ Support

If you enjoy the project: **[Buy me a coffee on Ko-fi](https://ko-fi.com/fabvittori)**.


## 📱 Dashboard predefinita / Default dashboard

Casa Dashboard Community include `examples/casa-dashboard-community-dashboard.yaml`, una plancia Lovelace bridge che richiama il pannello Community. Dopo averla aggiunta in **Impostazioni → Dashboard**, Home Assistant permette di impostarla come dashboard predefinita per tutti gli utenti o dal profilo del singolo utente. Nell'app Companion sarà quindi la dashboard aperta all'avvio.

> Home Assistant non espone un servizio ufficiale che consenta a una custom integration di cambiare automaticamente la dashboard predefinita dell'utente: la scelta finale va effettuata nelle impostazioni di Home Assistant.


## 📱 Tablet / kiosk mode

To open Casa Dashboard Community directly on a dedicated tablet/browser (Silk / Fully Kiosk), use:

```text
http://homeassistant.local:8123/casa-dashboard-community?kiosk=1
```

Replace `homeassistant.local:8123` with your Home Assistant address. `?kiosk=1` hides **Configure** and language controls.

The default Home Assistant dashboard is selected from Home Assistant settings/profile.
