# 🏠 Casa Dashboard Community

🇬🇧 **English** | [🇮🇹 Italiano](README.it.md)

[![Release](https://img.shields.io/badge/release-v3.5.1-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Add to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fabiovit&repository=casa-dashboard&category=integration)

Casa Dashboard Community is a complete app-like dashboard for **Home Assistant**, designed to adapt to different homes without relying on traditional Lovelace cards.

**v3.5.1** introduces the paged Casa V2 configurator, full visual customization, direct room/object photo uploads and the new Advanced Energy View, while keeping Casa V1 Classic fully available.

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

## ☀️ Advanced Energy View

Casa V2 can display the Solar section in **Compact** or **Advanced** mode.

Advanced mode provides an adaptive energy showcase with live solar production, optional PV1/PV2 strings, battery SOC and charge/discharge flow, plus Home / Inverter / Battery / Grid nodes.

Grid and battery sign conventions are configurable, so the view can adapt to different inverter integrations. Missing sensors are hidden automatically without leaving empty blocks.

## 🧭 Paged configurator

The Casa V2 configurator is split into dedicated pages:

- Overview
- Rooms
- Devices
- Energy & Mobility
- Weather & Security
- Advanced

This keeps normal configuration simple while moving the complete **173 optional Community mappings** into the Advanced page.

## 🎨 Full visual customization

Casa V2 can personalize:

- Overview macro labels;
- vehicle and Wallbox names;
- global entity display names;
- room names, types and icons;
- room photos;
- individual object/entity photos.

Photos can be uploaded directly from the configurator. Casa Dashboard resizes and compresses them automatically and normally stores them under `/config/www/casa_dashboard_community/uploads/`, referenced through `/local/casa_dashboard_community/uploads/`.

If no custom photo is configured, the normal Casa V2 generated visual and smart device recognition remain active.

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

The 173 Community mappings are **optional**. Configure only the functions and devices that exist in your Home Assistant installation.

Global mappings can also have a custom display name for the Overview. If left empty, Casa Dashboard uses the Home Assistant friendly name and then the Community fallback name.

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

The language selector is available in the dashboard and the selected language is stored locally. Custom room names and Home Assistant entity names are preserved.

## 📱 Responsive

Casa V1 and Casa V2 are designed for desktop, tablet and smartphone.

## 📦 HACS installation

1. Open **HACS**.
2. Add `https://github.com/fabiovit/casa-dashboard` as a custom repository of type **Integration**, or use the **Add to HACS** button above.
3. Install **Casa Dashboard Community**.
4. Restart Home Assistant.
5. Go to **Settings → Devices & services → Add integration**.
6. Search for **Casa Dashboard Community**.
7. Open the new sidebar panel and press **Configure**.

> After updating to v3.5.1, perform a **full Home Assistant restart** because the integration backend and WebSocket configuration schema have changed.

## 📦 Manual installation

Copy `custom_components/casa_dashboard_community` into `/config/custom_components/`, restart Home Assistant and add the integration from **Settings → Devices & services**.

## ℹ️ Notes

Casa Dashboard Community is an advanced template. Devices, sensors, automations, solar, EV and Wallbox are optional. Functions that are not configured are hidden automatically.

## 🙏 Credits

Special thanks to **Mario Pagano** for feedback and suggestions that helped improve the configurator, Overview customization and visual flexibility of Casa Dashboard Community.

## ☕ Support

If you enjoy the project: **[Buy me a coffee on Ko-fi](https://ko-fi.com/fabvittori)**.
