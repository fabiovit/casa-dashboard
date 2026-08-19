# 🏠 Casa Dashboard Community

🇬🇧 **English** | [🇮🇹 Italiano](README.it.md)

[![Release](https://img.shields.io/badge/release-v2.1.1-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Add to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fabiovit&repository=casa-dashboard&category=integration)

Casa Dashboard Community is an app-like dashboard for **Home Assistant**, built as a complete custom panel and designed to adapt to very different installations without relying on traditional Lovelace cards.

**Casa Dashboard Community v2.1.1** includes two visual experiences, **Casa V1** and **Casa V2**, dynamic rooms, in-dashboard entity configuration and native **English / Italian** language support.

The Community Edition uses the technical domain `casa_dashboard_community`, the panel `casa-dashboard-community` and the dedicated file `/config/www/casa-dashboard-community-entities.json`, so it can coexist with other Casa Dashboard installations without overwriting them.

**Created by Fabio Vittori** · [☕ Buy me a coffee](https://ko-fi.com/fabvittori)

# 🚀 Version 2.1.1

Version 2.1.1 adds native **English / Italian** language support directly inside the dashboard.

You can switch the interface language between:

- 🇬🇧 English
- 🇮🇹 Italiano

The selected language is remembered on the current browser/device.

Custom room names and Home Assistant entity names remain exactly as configured by the user.

## ✨ Casa V1 + Casa V2

### Casa V1 — Classic

The original Community interface remains available for users who prefer the classic experience from the 1.x series.

![Casa Dashboard Community - Casa V1 Classic](images/casa-v1-classic.png)

### Casa V2 — Dynamic

Casa V2 introduces a more visual experience with dedicated room scenes, contextual device visuals and an Overview focused on the information that actually matters.

> V2 screenshots show an example installation. Solar, EV, Wallbox and other devices are optional and only appear when configured.

#### V2 Overview

![Casa Dashboard Community - Casa V2 Overview](images/casa-v2-overview.png)

#### V2 Entrance

![Casa Dashboard Community - Casa V2 Entrance](images/casa-v2-ingresso.png)

#### V2 Garage

![Casa Dashboard Community - Casa V2 Garage](images/casa-v2-garage.png)

## 🏠 Dynamic rooms

With Casa V2, rooms are no longer tied to the structure of the original house.

You can:

- create new rooms;
- freely choose room names;
- select the room type;
- select the room icon;
- reorder rooms;
- remove unused rooms;
- create multiple rooms of the same type;
- assign multiple Home Assistant entities to the same room.

Visual room types include Kitchen, Bathroom, Bedroom, Living Room, Office, Laundry Room, Basement, Garage, Balcony/Terrace, Outdoor, Stairs, Entrance, Hallway and Generic Room.

## ⚙️ Advanced visual configurator

Configuration is handled directly from the dashboard using **Configure**.

Entities can be searched using:

- the Home Assistant assigned name (`friendly_name`);
- `entity_id`;
- a custom display name chosen inside Casa Dashboard Community.

Existing Community associations are imported into rooms during the first room configuration. After the first save, the Rooms section becomes the source of truth: entities manually removed from a room are not automatically added again.

The configurator also keeps the **173 Community logical mappings** used by global and specialized dashboard functions.

## 🏷️ Smart device recognition

Casa V2 uses multiple pieces of information to choose the most appropriate icon and visual:

1. custom display name;
2. Home Assistant friendly name;
3. recognized function;
4. Home Assistant icon;
5. `device_class`;
6. entity domain.

For example, a generic smart plug can be displayed as an **Air Fryer** if that is the name assigned to it.

Many categories are recognized, including lights, LED strips, sockets, air fryers, blenders/Thermomix, ovens, microwaves, dishwashers, washing machines, dryers, TVs, climate devices, air purifiers, dehumidifiers, gates, pedestrian gates, garage doors, blinds, shutters, robots, irrigation, robotic mowers, alarms, environmental sensors, Wallbox/EV, solar, inverters and batteries.

## 📊 V2 Overview

The new V2 Overview avoids duplicating the room list and focuses on:

- active states;
- main temperatures;
- outdoor and weather conditions;
- solar and battery;
- Wallbox and electric vehicle.

Sections with no useful configured entities remain hidden.

## 🌍 Languages

The dashboard interface can now be switched between:

- 🇬🇧 English
- 🇮🇹 Italiano

The language selector is available directly in the dashboard header.

The translation system covers Casa V1, Casa V2, the Overview, dynamic rooms, the configuration interface, the Information page and the main status/control labels.

Home Assistant entity names and custom room names are intentionally preserved.

## 🔄 Migration from the 1.x series

The update keeps the Community configuration separate.

During the first use of the new Rooms manager, existing Community mappings are used to initialize compatible rooms. After saving, rooms are managed directly by the new configuration.

**Casa V1 is not removed:** it remains selectable alongside Casa V2.

## 📱 Responsive

Both experiences are designed for desktop and mobile with adaptive menus and layouts.

## 📦 HACS installation

1. Open **HACS**.
2. Add `https://github.com/fabiovit/casa-dashboard` as a custom repository of type **Integration**, or use the **Add to HACS** button above.
3. Install **Casa Dashboard Community**.
4. Restart Home Assistant.
5. Go to **Settings → Devices & services → Add integration**.
6. Search for **Casa Dashboard Community**.
7. Open the dashboard and press **Configure**.

## 📦 Manual installation

1. Copy `custom_components/casa_dashboard_community` into `/config/custom_components/`.
2. Restart Home Assistant.
3. Add **Casa Dashboard Community** from **Settings → Devices & services**.
4. Open the dashboard and configure rooms and entities.

## ℹ️ Note

Casa Dashboard Community is an **advanced template**. Every Home Assistant installation is different: devices, sensors, automations, solar, EV and Wallbox are optional.

Unconfigured functions remain hidden.

## ☕ Support

If you like the project and want to support its development: **[Buy me a coffee on Ko-fi](https://ko-fi.com/fabvittori)**.
