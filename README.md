# 🏠 Casa Dashboard Community

🇬🇧 **English** | [🇮🇹 Italiano](README.it.md)

[![Release](https://img.shields.io/badge/release-v3.0.1-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Add to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fabiovit&repository=casa-dashboard&category=integration)

Casa Dashboard Community is a complete app-like dashboard for **Home Assistant**, designed to adapt to different homes without relying on traditional Lovelace cards.

**v3.0.1** is a consolidation release: the project has been cleaned up, versioning is now consistent across backend and frontend, and the mature features introduced in the 2.x generation are retained in a cleaner package.

**Created by Fabio Vittori** · [☕ Buy me a coffee](https://ko-fi.com/fabvittori)

## ✨ Casa V1 + Casa V2

### Casa V1 — Classic

The original Community experience remains available.

![Casa Dashboard Community - Casa V1 Classic](images/casa-v1-classic.png)

### Casa V2 — Dynamic

The configurable generation of Casa Dashboard. Rooms are created around your home rather than around the original author's house.

![Casa Dashboard Community - Casa V2 Overview](images/casa-v2-overview.png)

Additional examples:

![Casa Dashboard Community - Casa V2 Entrance](images/casa-v2-ingresso.png)

![Casa Dashboard Community - Casa V2 Garage](images/casa-v2-garage.png)

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
