# 🏠 Casa Dashboard Community

🇬🇧 **English** | [🇮🇹 Italiano](README.it.md)

[![Release](https://img.shields.io/badge/release-v4.0.0-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Add to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fabiovit&repository=casa-dashboard&category=integration)

Casa Dashboard Community is a complete app-like dashboard for **Home Assistant**, designed to adapt to different homes without relying on traditional Lovelace cards.

**v4.0.0** consolidates the current Dynamic generation into a cleaner, stable base with aligned frontend/backend versioning.

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

Dynamic rooms recognize `lock.*` and `alarm_control_panel.*` entities and can add dedicated lock/alarm controls when configured.

## ☀️ Advanced Energy View

Casa Dashboard 4.0 supports **Compact** and **Advanced** Solar views with live production, optional PV1/PV2 strings, battery SOC and charge/discharge flow, plus Home / Inverter / Battery / Grid nodes.

Grid and battery sign conventions are configurable to adapt to different inverter integrations.

## 🔗 Shared room modules

Configure global data once and reuse it inside rooms without duplicating mappings:

- Solar Energy
- EV + Wallbox
- Weather
- Alarm

## 🧭 Paged configurator

The configurator is split into dedicated pages:

- Overview
- Rooms
- Devices
- Energy & Mobility
- Weather & Security
- Advanced

## 🎨 Visual customization

Customize Overview labels, vehicle and Wallbox names, room images, entity names, icons and object photos.

Uploaded entity photos are resized and stored under `/local/casa_dashboard_community/uploads/`.

## 🏠 Dynamic rooms

Casa Dashboard 4.0 lets you create, rename, reorder and remove rooms, choose room type/icon and assign multiple Home Assistant entities to each room.

## ⚙️ Visual configurator

Entities can be searched by Home Assistant friendly name, `entity_id` or custom display name. Large installations are supported with dedicated scrolling and grouped configuration pages.

## 🧠 Smart device recognition

Casa Dashboard can choose a suitable visual using custom name, Home Assistant friendly name, recognized function, HA icon, `device_class` and entity domain.

## 📊 Overview

The Overview focuses on active states, temperatures, weather, solar/battery, grid data, Wallbox and optional electric vehicle data. Unconfigured sections remain hidden.

## 🌍 Languages

Native interface support:

- 🇬🇧 English
- 🇮🇹 Italiano

The selected language is stored locally. Custom room and Home Assistant entity names are preserved.

## 📱 Responsive

Casa Dashboard 4.0 is designed for desktop and mobile.

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

Devices, sensors, automations, solar, EV and Wallbox are optional. Unconfigured functions are hidden automatically.

## ☕ Support

If you enjoy the project: **[Buy me a coffee on Ko-fi](https://ko-fi.com/fabvittori)**.
