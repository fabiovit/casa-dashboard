# Changelog

## 4.2.7 - 2026-09-01

- Upgraded `?kiosk=1` to use Home Assistant native kiosk mode.
- Kiosk now hides the Home Assistant sidebar/menu in addition to Casa Dashboard configuration and language controls.
- Kiosk state is restored automatically when leaving the panel.
- Hid the dashboard Home Assistant menu button while kiosk mode is active.
- Minor frontend cleanup and version consistency pass.

## 4.2.6 - 2026-09-01

### Release Candidate - cleanup and consolidated responsive layer

- Consolidated the accumulated late responsive overrides into one authoritative layer.
- Fixed mobile chapter/title grid collapse.
- Normalized phone-width cards and custom-photo geometry.
- Kept one smart-lock renderer and preserved its Home Assistant control path.
- Localized generic toggle labels in Italian mode.
- Preserved tester-driven Overview controls, Active States groups, ordering, icon preview and kiosk mode.
- Removed stale release notes and build debris.

## 4.2.5 - 2026-09-01

### SAFE TEST — real smartphone responsive pass

- Fixed chapter grid after hiding its decorative line.
- Rebuilt mobile header geometry instead of only reducing font size.
- Forced room device cards to usable full width on smartphones.
- Normalized smart-lock and specialist photo cards.
- Reduced solar and battery visuals specifically for phone widths.
- Improved Active States and Robot Overview mobile containment.

## 4.2.4 - 2026-09-01

### SAFE TEST — structural renderer fixes

- Rebuilt from v4.2.2 instead of layering over v4.2.3.
- Fixed smart-lock renderer without creating duplicate cards.
- Added photo/size/localized-state support to the original lock card.
- Normalized media_player/Alexa and climate cards.
- Expanded Italian state translations.
- Added actual-state refresh in Active States and covers group.
- Reduced advanced solar renderer using exact classes.
- Made Compact headers genuinely compact on smartphones.
- Constrained sensor/robot/mower photos within card bounds.
- Reworked Overview panels and mobile title formatting.

## 4.2.2 - 2026-09-01

### SAFE TEST

- Reintroduced remaining tester requests on the stable v4.2.1 runtime.
- Added configurable Overview visibility and sizing.
- Added grouped Active States with popup controls.
- Added room entity ordering and icon previews.
- Extended custom photos and robot naming.
- Added tablet/kiosk mode via `?kiosk=1`.
- Kept the 19-part loader and no new background observers/timers.

## 4.2.1 - 2026-08-31

### Emergency stability hotfix

- Rolled back the v4.2 frontend renderer to the stable v4.1.2 runtime.
- Preserved v4.2 backend configuration compatibility.
- Preserved saved room fields such as title size, subtitle and entity order.
- Kept the stable 19-part frontend loader.
- Prepared a stable base for reintroducing v4.2 features incrementally.

## 4.2.0 - 2026-08-31

### Community tester UX overhaul

- Dedicated mobile density and smaller hero titles.
- Per-room title size, optional subtitle and custom subtitle.
- Overview sections can be hidden and assigned a visual size.
- Section headings use readable surfaces over custom backgrounds.
- Active states are grouped and actionable directly from Overview.
- Common entity states are localized in Italian.
- Custom photos extended to vacuum and lawn mower entities and hardened on mobile.
- Room entity order can be changed; default ordering is grouped by entity type.
- Custom light icons are now rendered in the light visual itself.
- Background color/gradient persistence from 4.1.2 retained.
- Robot overview naming respects configured/friendly names.
- Added an official-style Lovelace bridge example so Casa Dashboard Community can be selected as Home Assistant's default dashboard.

## 4.1.2 - 2026-08-28

### Background persistence fix

- Fixed solid background color values not being persisted correctly.
- Fixed gradient Color 1 / Color 2 / Angle values not being saved.
- Fixed room background controls not being copied during final save.
- Improved background controls so selections survive tab changes.
- Backend now safely preserves numeric overview configuration values.

## 4.1.1 - 2026-08-28

- Added real color pickers for solid dashboard and room backgrounds.
- Added two-color gradient controls with configurable angle.
- Improved readability over photographic backgrounds.
- Fixed room backgrounds so the Overview background no longer leaks through while scrolling.
- Added Home Assistant `lawn_mower` support with start and dock controls.
- Preserved all v4.1.0 improvements.

## 4.1.0 - 2026-08-28

- Added per-entity size controls.
- Made solar and battery sections more compact on mobile.
- Improved smartphone photo decoding and EXIF orientation support.
- Expanded mobile image picker compatibility.


### Tester improvements

- Expanded icon library and added state-aware lighting visuals.
- Fixed lampadina/plafoniera visual duplication.
- Added room filter to Devices configurator.
- Fixed custom photos on cover / blind / awning entities.
- Improved configurator scroll-position persistence after edits/removals.
- Removed room-name based rendering: room type is now the only renderer selector.
- Added global and per-room backgrounds: automatic, solid color, gradient or image.
- Kept Overview/Home fixed in the top navigation while rooms scroll independently, with arrow controls.
- Removed duplicate EV data from the Wallbox strip when only vehicle mappings are configured.
- Improved electric vehicle visual presentation.
- Added vacuum/cleaning robot rendering in rooms and Overview.
- Preserved shared Solar, EV + Wallbox, Weather and Alarm modules.

## 4.0.0 - 2026-08-27

### Major Community Release

- Promoted the current stable Community generation to **4.0.0**.
- Preserved the dynamic room architecture and paged configurator.
- Preserved shared reusable room modules for **Solar Energy**, **EV + Wallbox**, **Weather** and **Alarm**.
- Preserved the advanced Solar view with PV1/PV2, battery, house load and grid flow.
- Preserved improved Weather presentation shared between Overview and rooms.
- Preserved the advanced **EV + Wallbox** room console and separate real EV vehicle data.
- Preserved room-specific visuals, custom entity icons/photos, blinds/awnings, climate layout and alarm panel.
- Preserved light/dark themes, responsive layout and IT/EN interface.
- Performed a conservative source cleanup without changing runtime behavior.
- Kept the stable 19-part frontend loader architecture.
- Versioning aligned across frontend loader, integration backend and manifest.

## 3.9.7 - 2026-08-27

### EV Vehicle in Mobility Rooms

- Rooms using the **EV + Wallbox** shared module now also show the configured electric vehicle card.
- Vehicle data remains independent from Wallbox data and uses only real `sensor.vehicle_*` mappings.
- If no vehicle mappings are configured, only the Wallbox console is rendered.
- Added battery, range, remaining charge time, charging power, session energy and odometer metrics when available.
- No additional room module is required: vehicle data follows the existing EV + Wallbox module.
- Preserved all previous fixes and the stable 19-part frontend loader.

## 3.9.6 - 2026-08-27

### Auto elettrica separata da EV + Wallbox

- Aggiunto il gruppo **Auto elettrica** in Energia & Mobilità.
- I mapping veicolo esistenti sono ora visibili nel configuratore.
- La card Auto in Panoramica compare solo con almeno un vero mapping `sensor.vehicle_*`.
- Rimossi i fallback a potenza ed energia sessione della Wallbox.
- EV + Wallbox resta indipendente.

## 3.9.5 - 2026-08-27

### Generic EV + Wallbox Naming

- Renamed the Community mobility module from **BYD + DAZE** to **EV + Wallbox**.
- Kept the subtitle **Ricarica domestica**.
- Removed personal-brand references from status and diagnostic labels.
- **STATO DAZE** is now **STATO WALLBOX**.
- EVSE subtitle is now generic: **Veicolo elettrico**.
- Diagnostic label **Ventola DAZE** is now **Ventola wallbox**.
- Preserved the advanced mobility visual introduced in v3.9.4.
- Preserved Weather, Solar and shared-module persistence fixes.
- Preserved stable 19-part frontend loader.

## 3.9.4 - 2026-08-27

### BYD + DAZE Room Module Visual Parity

- Reworked the **Wallbox & EV** room module to match the personal Casa Dashboard BYD + DAZE console.
- Added dedicated car + wallbox visual with live charging LED and charging/rest status.
- Added primary cards for Charging Power, Meter Load, Session Energy, Charging Limit, DAZE Status and EVSE Status.
- Meter load is derived from configured Grid Current L1 × Wallbox Voltage L1.
- Charging limit power is derived from configured Max Charging Current × Wallbox Voltage L1.
- Added DAZE diagnostic cards for board temperature, case temperature and fan status when configured.
- Uses only the global Wallbox & EV mappings already configured in Community.
- Preserved v3.9.3 Weather parity, v3.9.2 Solar parity and v3.9.1 module persistence.
- Preserved stable 19-part frontend loader.

## 3.9.3 - 2026-08-27

### Weather Room Module Visual Parity

- The **Meteo** room module now reuses the same weather data/presentation as Overview.
- Removed the generic technical metric grid from room Weather modules.
- Added a richer weather presentation with dedicated icon blocks, stronger hierarchy and responsive layout.
- Outdoor temperature, humidity, wind, rain, solar radiation/lux, UV and pressure remain driven by the globally configured Weather mappings.
- Weather visual improvements are shared by Overview and room modules to avoid duplicate renderers.
- Preserved v3.9.2 Solar renderer parity and v3.9.1 module persistence fixes.
- Preserved stable 19-part frontend loader.

## 3.9.2 - 2026-08-27

### Solar Room Module Visual Parity

- The **Energia solare** room module now reuses the exact same advanced solar renderer used in Overview.
- Room and Overview now share identical PV production, PV1/PV2, battery, house load and grid visuals.
- Battery charge/discharge direction, grid import/export signs and custom energy labels are now identical everywhere.
- Daily charge, discharge and loss pills are reused from the Overview renderer.
- Removed the generic metric-grid presentation for Solar inside rooms.
- Wallbox & EV, Weather and Alarm remain reusable shared modules.
- Preserved v3.9.1 module persistence fixes and all previous features.
- Preserved stable 19-part frontend loader.

## 3.9.1 - 2026-08-27

### Shared Room Module Persistence Fix

- Fixed room module selections not reliably surviving Save / configurator reopen.
- Module checkboxes now update the room draft immediately on change.
- `syncRooms()` now explicitly captures all selected room modules before tab switches and save.
- Final Save still performs a defensive module synchronization.
- Added room-module loading to the JSON fallback path.
- Added explicit visual selected state for persisted modules.
- Backend module sanitization and persistence verified.
- Preserved all v3.9.0 reusable modules and previous fixes.
- Preserved stable 19-part frontend loader.

## 3.9.0 - 2026-08-27

### Reusable Room Modules

- Added reusable room modules for **Energia solare**, **Wallbox & EV**, **Meteo** and **Allarme**.
- Modules reuse the global mappings already configured in Energy & Mobility / Weather & Security.
- Rooms store only the selected module IDs: entity mappings are not duplicated.
- Changing a global mapping automatically updates every room using the corresponding module.
- Added module selectors directly to each room in the Rooms configurator page.
- Preserved v3.8.1 awning visuals, v3.8.0 smart auto-mapping and previous fixes.
- Preserved stable 19-part frontend loader.

## 3.8.1 - 2026-08-27

### Awning / Tenda Visual Parity

- Added dedicated awning cards matching the personal Casa Dashboard.
- Tenda / awning cover entities now use cassette, fabric and articulated-arm graphics instead of generic blind/shutter cards.
- Retracted state is shown as **Raccolta**.
- Fully extended state is shown as **Estesa**.
- Intermediate positions display the actual percentage.
- Added **Gestisci tenda** button opening Home Assistant more-info controls.
- Works in Kitchen and generic dynamic rooms.
- Preserved v3.8.0 smart auto-mapping and all previous fixes.
- Preserved stable 19-part frontend loader.

## 3.8.0 - 2026-08-27

### Smart Auto Mapping

- Added **Abbina automaticamente** to mapping pages.
- Existing manual mappings are never overwritten.
- Empty mappings are matched against entities already assigned to rooms first.
- If no safe room match exists, the complete Home Assistant entity registry is considered.
- Matching considers room name/type, entity domain, `device_class`, unit, friendly name and `entity_id`.
- Added dedicated scoring for temperature, humidity, illuminance, movement/presence, openings, climate, lights, alarm, EV/Wallbox, solar/inverter/battery and weather entities.
- Low-confidence matches are deliberately skipped instead of guessed.
- The configurator reports how many associations were proposed before saving.
- Preserved v3.7.9 fan visuals, v3.7.8 Overview and v3.7.7 icon persistence.
- Preserved stable 19-part frontend loader.

## 3.7.9 - 2026-08-27

### Fan / Extractor Visual Parity

- Added the large physical four-blade fan visual used by the personal Casa Dashboard.
- Fan-domain entities now automatically use the dedicated fan visual.
- Switch entities named Aspiratore / Ventilatore / Ventola also use the dedicated visual.
- Selecting the custom icon **Ventola** (`mdi:fan`) forces the same dedicated visual even for a switch entity.
- OFF state now displays **Spento**, matching the personal dashboard.
- ON state displays **Attivo** and animates the rotor.
- Preserved all v3.7.8 Overview improvements and v3.7.7 custom-icon persistence fixes.
- Preserved stable 19-part frontend loader.

## 3.7.8 - 2026-08-27

### Overview Climate & Weather Parity

- Reworked Casa V2 Overview climate section to follow the personal Casa Dashboard.
- Added one compact climate card per indoor room with temperature and optional humidity.
- Added the Outdoor climate card to the same Climate House row when available.
- Humidity entities can no longer be misclassified as temperatures.
- Added dedicated Weather overview with Outdoor temperature, Wind, Rain, Solar radiation and UV when available.
- Weather secondary data can show outdoor humidity, lux and pressure where available.
- Removed duplicated generic room sensor cards from the Overview climate area.
- Preserved custom icon persistence fixes from v3.7.7.
- Preserved stable 19-part frontend loader.

## 3.7.7 - 2026-08-27

### Custom Icon Save Path Fix

- Fixed the real icon persistence bug in `_saveConfigDialog()`.
- The Save Configuration action now reads every per-device icon selector immediately before sending the WebSocket payload.
- Previously, icon changes could exist only in the live configurator UI and never reach the saved room payload.
- Added post-save room normalization so returned `entity_icons` remain in frontend state immediately.
- Backend `entity_icons` read/write support remains verified.
- Preserved all v3.7.6 and v3.7.4 features.
- Preserved the stable 19-part frontend loader.

## 3.7.6 - 2026-08-27

### Custom Icon Persistence — Definitive Fix

- Fixed the configurator draft clone dropping `entity_icons` when reopening configuration.
- Added `entity_icons` to the room copy created by `_openConfigDialog()`.
- Added defensive icon synchronization before tab changes and save.
- Audited room clone paths so labels, images and icons travel together.
- Backend `entity_icons` persistence remains enabled and verified.
- Custom icons now survive Save, configurator reopen and dashboard reload.
- Preserved all v3.7.5 / v3.7.4 features.
- Preserved the stable 19-part frontend loader.

## 3.7.5 - 2026-08-27

### Per-device Icon Persistence Fix

- Fixed custom device icons reverting to Automatic after saving/reloading the configurator.
- Preserved `entity_icons` through every room normalization and cloning path.
- Ensured `entity_icons` are restored from the backend configuration.
- Ensured per-device icon changes refresh the room draft state before save.
- Added defensive frontend normalization for labels, images and icons.
- Confirmed backend persistence of `entity_icons`.
- Preserved all v3.7.4 Disimpegno and appliance visual improvements.
- Preserved the stable 19-part frontend loader.

## 3.7.4 - 2026-08-27

### Dynamic Hallway / Disimpegno

- Added a dedicated Casa V2 renderer for Disimpegno / Corridoio rooms.
- Separated Lights from Devices & Appliances.
- Added a dedicated Control & Sensors section.
- Added semantic appliance visuals for dryer, washing machine, dishwasher, refrigerator, dehumidifier, purifier, vacuum, plugs and siren.
- Dryer now uses a proper `mdi:tumble-dryer` visual instead of the generic device icon.
- Hallway hero now focuses on movement and occupancy.
- Motion / occupancy visuals remain live-updating.
- Preserved all v3.7.3 FIXED climate and Overview corrections.
- Preserved the stable 19-part frontend loader.

## 3.7.3 - 2026-08-27

### Ambient Sensor Priority + Stability Fix

- Kitchen Comfort & Climate prioritizes a real room temperature sensor over `climate.current_temperature`.
- Room humidity sensor also has priority over climate-provided humidity.
- Improved automatic recognition of ambient temperature/humidity sensors.
- Kept the proven Community climate panel CSS from v3.7.2.
- Removed the direct personal-dashboard CSS import that could destabilize the frontend.
- Preserved all v3.7.2 Overview room-priority and Kitchen runtime fixes.
- Preserved the stable 19-part frontend loader.

## 3.7.2 - 2026-08-27

### Kitchen Runtime & Overview Room-Priority Fix

- Restored the missing Kitchen Comfort & Climate renderer that prevented the Kitchen page from opening.
- Added full runtime dependency validation for the Kitchen renderer.
- Room assignment now has priority over legacy 173-entity mappings when classifying Overview data.
- Indoor room sensors can no longer appear in External / Weather only because of an old weather mapping.
- Kitchen temperature and humidity remain associated with the Kitchen and no longer leak into External.
- Outdoor-room entities are explicitly recognized as External.
- Solar classification now ignores accidental legacy-key matches for indoor room devices.
- Temperature classification now uses the real entity/name semantics for technical exclusions.
- Preserved all v3.7.1 filtering and v3.7.0 Community improvements.
- Preserved the stable 19-part frontend loader.

## 3.7.1 - 2026-08-27

### Overview Entity Classification Fix

- Fixed room appliances incorrectly appearing in the Overview Mobility / Wallbox section.
- Mobility now accepts only genuine EV / Wallbox / charging semantics.
- Added explicit protection against Kitchen appliance entities being classified as mobility devices.
- Tightened Overview Temperature filtering to exclude Wallbox / inverter / board / case temperatures.
- Tightened External / Weather classification.
- Tightened Solar / Battery / Grid classification.
- Room assignment no longer causes unrelated entities to leak into Overview categories.
- Preserved all v3.7.0 Community feedback improvements.
- Preserved the stable 19-part frontend loader.

## 3.7.0 - 2026-08-27

### Community Feedback Update

Based on community feedback from Mario Pagano:

- Added custom house photo to Casa V2 Overview.
- Added custom vehicle photo to the new EV overview.
- Added a broad per-device icon selector in the room configurator.
- Preserved semantic Open / Closed states for contact sensors.
- Moved the Configure action to the top bar and Information page; removed the large Overview configuration banner.
- Removed room icons from room hero titles while preserving icons in the top navigation.
- Improved room hero/photo responsiveness on smartphones to avoid clipped photos and room names.
- Fixed Overview metric cards to use configured custom display names, including Wallbox/EV fields.
- Added richer vehicle mappings: battery level, range, remaining charging time, odometer, charging power and session energy.
- Added a dedicated Auto EV Overview card with charge state, range, remaining time, energy and optional vehicle photo.
- Added persistent per-entity icon overrides to room configuration.
- Preserved the stable 19-part frontend loader.

## 3.6.9 - 2026-08-27

### Kitchen Semantic Appliance Icons

- Added dedicated semantic icon recognition for Kitchen appliances and powered devices.
- Added specific visuals for refrigerator, dishwasher, microwave, oven, coffee machine, Mac mini, monitor, camera, USB outlets, handheld vacuum, Home Assistant, hubs, empty outlets and siren.
- Existing dedicated visuals for hood, Bimby/Thermomix, Airfryer and TV are preserved.
- Generic Kitchen devices now use the appliance visual style instead of generic control cards.
- Increased appliance rendering limit to 12 additional devices.
- Preserved Kitchen section structure and climate panel from v3.6.8.
- Preserved stable 19-part frontend loader.

## 3.6.8 - 2026-08-27

### Kitchen Climate Panel Visual Parity

- Replaced the generic Kitchen climate card with a dedicated large Comfort & Climate panel.
- Added ambient-temperature ring.
- Added Setpoint, Humidity and Fan summary cards.
- Added dedicated Climate Status row.
- Added large **Open climate panel** action.
- Layout now closely follows Casa Dashboard v5.4.0.
- Preserved Kitchen section order introduced in v3.6.7.
- Preserved stable 19-part frontend loader.

## 3.6.7 - 2026-08-27

### Kitchen Section Structure & Blind Support

- Added a dedicated **Tenda** section for every `cover.*` assigned to the Kitchen.
- Added blind visual, current position and Open / Close control.
- Reorganized the Kitchen in a fixed semantic order:
  1. Lights
  2. Comfort & Climate
  3. Blind
  4. Appliances
  5. Heating & DHW
  6. Environment
  7. Sensors
- Lights are no longer mixed with appliances.
- Climate is no longer mixed with heating.
- Appliances are rendered in their own dedicated section.
- Preserved all live-state, sensor-ordering and Security & Access fixes.
- Preserved the stable 19-part frontend loader.

## 3.6.6 - 2026-08-27

### Kitchen Lights & Climate Fix

- Kitchen now renders every `light.*` assigned to the room, not only the first light.
- LED strips and LED lights are therefore preserved automatically.
- Added semantic LED / strip icon recognition.
- Separated room air-conditioning from heating climate entities.
- Added a dedicated **Clima cucina** section with full climate controls.
- Heating & DHW now appears only for an explicitly recognized heating / thermostat entity.
- Prevented a single air conditioner from being incorrectly reused as the home-heating device.
- Preserved the dedicated Kitchen renderer and stable 19-part loader.

## 3.6.5 - 2026-08-27

### Kitchen Runtime Fix

- Fixed Casa V2 Kitchen page failing to open.
- Replaced an invalid `_roomEntityLabel()` call with the existing Community `_roomEntityCustomLabel()` helper.
- Added the missing Kitchen appliance visual helper required by the dedicated Kitchen renderer.
- Added a runtime dependency audit for the Kitchen renderer to ensure all referenced methods are present.
- Preserved the dedicated Kitchen layout introduced in v3.6.4.
- Preserved the stable 19-part frontend loader.

## 3.6.4 - 2026-08-27

### Dynamic Kitchen Layout

- Added a dedicated Casa V2 dynamic Kitchen renderer inspired by Casa Dashboard v5.4.0.
- Added Kitchen hero with live environment and activity summary.
- Kitchen devices are now grouped into a compact appliance section.
- Added semantic recognition for hood, cooking robot/Thermomix, air fryer and TV.
- Added dedicated Heating & DHW section when climate / water-heater entities are available.
- Added dedicated Kitchen Environment section for temperature, humidity, climate temperature and illuminance.
- Added dedicated Kitchen Sensors section for doors/windows, vibration and motion.
- Preserved semantic sensor visuals and live updates.
- Preserved stable 19-part frontend loader.

## 3.6.3 - 2026-08-27

### Sensor Ordering

- Added semantic sensor ordering inside Casa V2 dynamic rooms.
- Sensors are now displayed in this order:
  1. Doors
  2. Windows
  3. Illuminance
  4. Temperature
  5. Motion / Occupancy
  6. Other sensors
- Ordering is based on both Home Assistant `device_class` and entity/display names for better compatibility.
- Entities within the same category are sorted alphabetically.
- Preserved all Security & Access, live refresh and visual parity fixes from v3.6.2.

## 3.6.2 - 2026-08-27

### Entrance Visual Parity Fix

- Added Entrance fallback to the globally configured door-lock mapping when the lock is not explicitly assigned to the room.
- Added Entrance fallback to the globally configured alarm mapping.
- Fixed missing CSS for door/opening visual cards.
- Fixed missing CSS for environment sensor visual cards.
- Security & Access now expands correctly when only one security device is available.
- Adjusted Security & Access proportions to more closely match Casa Dashboard v5.4.0.
- Preserved live room-state refresh fix from v3.6.1.
- Preserved the stable 19-part frontend loader.

## 3.6.1 - 2026-08-27

### Live Room State & Visual Parity Fix

- Fixed Casa V2 room entities not always triggering a visual refresh when their state changed.
- State fingerprint now includes every entity assigned directly to dynamic rooms, not only the 173 global mappings.
- Motion, occupancy and vibration entities now use the same visual activity cards as the original Casa Dashboard.
- Door/window/opening entities use semantic open/closed visuals instead of raw `on` / `off`.
- Temperature, humidity and illuminance sensors use dedicated environment visuals.
- Added support for lock-like `input_boolean` entities in Security & Access, in addition to native `lock.*`.
- Prevented lock-like entities from being duplicated in the generic device section.
- Preserved the stable 19-part frontend loader and all v3.6.0 SAFE behavior.

## 3.6.0 - 2026-08-27

### Security & Access

- Added native `lock.*` recognition to Casa V2 dynamic rooms.
- Added native `alarm_control_panel.*` recognition to Casa V2 dynamic rooms.
- Added adaptive Security & Access section inspired by the original Casa Dashboard.
- Added Lock / Unlock controls.
- Added alarm Home / Away / Off quick controls.
- Added security information to the room hero when available.
- Added contextual warning when a configured door is closed but the lock remains unlocked.
- Security blocks disappear automatically when not configured.
- Sensor section now includes the room name.
- Improved feedback during slower configuration saves.
- Preserved the proven 19-part frontend loader from v3.5.3.
- Preserved image upload, room creation, scroll memory and Advanced Energy View.

## 3.5.3 - 2026-08-26

### Image Upload Flow Fix

- Preserved configurator scroll position after edits, entity changes, photo actions and rerenders.
- Added per-tab scroll memory so returning to a configurator section restores the previous position.
- Restored the **Add room** controls in the paged Rooms configurator (top and bottom of the room list).
- Fixed the post-selection image flow appearing to do nothing after choosing a file.
- Images are now compressed to a small inline preview first and immediately stored in the configuration draft.
- Preview appears immediately before backend file upload completes.
- Backend `/local/...` upload now runs only as an optimization; failure no longer discards the selected image.
- Added visible upload states: processing, acquired, verified, fallback-ready and error.
- Added 7-second backend upload timeout and 3.5-second URL verification timeout to prevent silent hangs.
- Inline fallback target reduced to ~260 KB to keep configuration saves reliable.
- Preserved all v3.5.2 image format, compression and Advanced Energy features.

## 3.5.2 - 2026-08-26

### Robust Image Upload Hotfix

- Replaced the programmatic hidden file picker with native per-button file inputs for reliable operation in Home Assistant WebView/Desktop environments.
- Reduced normal image upload payloads to a safe target of about 700 KB.
- Images are progressively resized/compressed as JPEG up to 1200 px on the longest side.
- Added a smaller ~420 KB inline fallback to avoid oversized Community configuration payloads.
- Added post-upload verification: `/local/...` images are accepted only if they are actually reachable.
- Added backend verification that the file was physically written correctly.
- Original photos up to 20 MB are accepted because compression happens before upload.
- Added HEIC/HEIF selection with a clear compatibility message when the browser cannot decode the format.
- Added clearer upload-success feedback in the configurator.
- JPG/JPEG, PNG and WebP remain the recommended formats.
- Preserved all v3.5.1 Advanced Energy View and configurator functionality.

## 3.5.1 - 2026-08-26

### Image Upload Reliability Fix

- Fixed room and per-object photos not being retained in some installations.
- Added a resilient image storage fallback when the dedicated upload WebSocket command is not yet available.
- Preferred storage remains `/config/www/casa_dashboard_community/uploads/` with a `/local/...` URL.
- Fallback images are resized/compressed and stored directly in the Community configuration as a Data URL.
- Added immediate image previews for room photos and individual object photos.
- Added WebSocket command registration safety in `async_setup_entry`.
- Fixed Overview radio/select persistence during configuration save.
- Preserved all v3.5.0 Advanced Energy View features.

## 3.5.0 - 2026-08-26

### Advanced Energy View

- Added Compact / Advanced Solar display selection in Casa V2.
- Added advanced live-production card inspired by the current personal Casa Dashboard energy design.
- Added optional PV1 and PV2 production bars with voltage/current details when configured.
- Added battery SOC visual with charge/discharge power and optional daily energy details.
- Added adaptive Home / Inverter / Battery / Grid energy nodes.
- Added configurable labels for production, PV1, PV2, Home, Inverter, Battery and Grid.
- Added configurable positive-sign convention for Grid import/export.
- Added configurable positive-sign convention for Battery charge/discharge.
- Advanced layout automatically removes unavailable PV strings, battery or grid data without leaving empty blocks.
- Preserved Compact mode for users who prefer the simpler Overview.
- Fixed configurator event wiring so room/object image upload remains available independently of the search field.
- Preserved all v3.4.0 paged-configurator functionality.

## 3.4.0 - 2026-08-26

### Configurator Redesign

- Rebuilt the Casa V2 configurator as a paged/tabbed interface.
- Added dedicated pages for Overview, Rooms, Devices, Energy & Mobility, Weather & Security and Advanced mappings.
- Separated room structure management from per-room entity/device management.
- Moved the full 173 Community mappings into the Advanced page.
- Energy and Weather/Security pages now expose only relevant mappings.
- Kept Save/Cancel controls fixed and available from every page.
- Preserved direct image upload for rooms and individual objects.
- Preserved custom Overview labels, vehicle/Wallbox naming and all existing v3.3.0 functionality.
- Improved mobile configurator navigation and reduced visual clutter.

## 3.3.0 - 2026-08-26

### Direct Photo Upload & Object Images

- Added direct room-photo upload from the Casa V2 configurator.
- Added custom photos for individual V2 objects/entities: lights, switches, appliances, sensors and other devices.
- Photos are resized/compressed in the browser before upload.
- Uploaded files are stored safely in `/config/www/casa_dashboard_community/uploads/`.
- The configuration stores only the `/local/...` image path.
- Per-object images are stored per room.
- Custom photos override generated visuals only when explicitly configured.
- Automatic Casa V2 visuals and smart recognition remain the fallback.
- Supported uploads: JPEG, PNG and WebP.
- Preserved all v3.2.0 macro-label, Auto/Wallbox naming and room-photo features.

## 3.2.0 - 2026-08-26

### Full Visual Customization

- Added customizable macro labels for the Casa V2 Overview.
- Added customizable Overview title.
- Added independent custom names for the electric vehicle and Wallbox.
- Mobility section automatically uses the configured Auto / Wallbox names when no custom macro label is set.
- Added per-room custom image support in Casa V2.
- Room images accept Home Assistant `/local/...` paths, absolute paths or HTTP/HTTPS image URLs.
- Custom room image fallback order: custom photo → Casa V2 generated room visual.
- Room image settings are stored persistently in the Community configuration.
- Overview customization is stored persistently and survives restarts/upgrades.
- Preserved custom entity display names and all v3.1.0 adaptive Overview improvements.
- Based visually on the current Casa Dashboard personal design while keeping Community entities and configuration completely independent.

## 3.1.0 - 2026-08-26

- Special thanks to **Mario Pagano** for feedback and suggestions that helped improve the v3.1.0 Overview and configurator experience.

- Added custom **display names for global Overview mappings**, using the same concept already available for Casa V2 room entities.
- Overview naming priority is now: custom display name → Home Assistant friendly name → Community fallback name.

### Adaptive Community Overview

- Redesigned V2 Overview cards so partially configured installations remain visually complete and balanced.
- Fixed low contrast / nearly invisible Overview cards when Home Assistant uses a light theme.
- Overview grids now adapt automatically to the number of available metrics.
- Added visual icons and stronger card hierarchy for Solar, Battery, Grid, Weather and Wallbox/EV metrics.
- Normalized power display: W values are automatically converted to kW and power values are limited to two decimals.
- Improved formatting for battery percentage, temperature, energy and generic numeric sensors.
- Binary EV/Wallbox states are displayed as readable Active/Inactive labels.
- Replaced the misleading “entity configuration incomplete” notice.
- The dashboard now explicitly explains that the 173 mappings are optional and users only need to configure the functions they use.

## 3.0.1 - 2026-08-26

### Home Assistant compatibility hotfix

- Fixed first configuration failure on Home Assistant versions where `frontend.async_panel_exists` is unavailable.
- Panel existence is now checked through Home Assistant's registered `frontend_panels` mapping.
- Applied the same compatibility logic during integration unload/reload.
- Prevents `AttributeError: module 'homeassistant.components.frontend' has no attribute 'async_panel_exists'`.
- No dashboard configuration or user data is changed.

## 3.0.0 - 2026-08-26

### Major cleanup and consolidation

- Unified integration, frontend and panel versioning to **3.0.0**.
- Removed stale internal version references left from the 1.x series.
- Preserved both **Casa V1 — Classic** and **Casa V2 — Dynamic**.
- Preserved dynamic rooms, room reordering, custom names, icons and multi-entity assignment.
- Preserved smart device recognition based on display name, friendly name, icon, device class and entity domain.
- Preserved the 173 Community entity mappings and the in-dashboard configurator.
- Preserved the balanced configurator scrolling introduced in the 2.1.x series.
- Preserved native **Italian / English** interface support and local language preference.
- Removed obsolete standalone release-note files from the repository root; release history remains in this changelog.
- Removed cache/build artifacts and verified the package structure for HACS distribution.
- Refreshed English and Italian documentation for the 3.0 generation.

## 2.1.2 - 2026-08-19

- Fixed configurator scrolling with large room and entity configurations.
- Rooms now use a dedicated, height-limited scroll area so they cannot consume the whole dialog.
- The 173 entity mappings always retain a useful minimum visible area with independent scrolling.
- Header, search toolbar and bottom action bar remain accessible.
- Improved layout and touch scrolling on desktop, mobile and Home Assistant webviews.

## 2.1.1 - 2026-08-19

- Fixed IT / EN language selector not activating reliably in Home Assistant.
- Language buttons now use dedicated click handlers instead of the global dashboard event delegation.
- Hardened DOM translation for Home Assistant webviews by avoiding dependency on an unqualified `NodeFilter` global.
- Language switching now performs a clean interface rebuild and reapplies the selected translation.
- Language preference remains stored locally on the browser/device.

## 2.1.0
- Added built-in Italian / English interface support.
- Added IT / EN language selector in the dashboard header.
- Language preference is saved locally per browser/device.
- Added English translations across Casa V1, Casa V2, Overview, dynamic rooms, configurator, information, weather, energy and EV/wallbox UI.
- Preserved Home Assistant friendly names, entity IDs and custom user room/device names.
- Existing 2.0.0 configuration remains compatible.


## 2.0.0 - 2026-08-18

- Introdotte **Casa V1 — Classic** e **Casa V2 — Dynamic**.
- Casa V1 resta disponibile e condivide la configurazione con Casa V2.
- Aggiunto il nuovo sistema di **stanze dinamiche**: creazione, rinomina, tipo, icona, riordino ed eliminazione.
- Aggiunta associazione multipla di entità Home Assistant alle stanze.
- Migliorata la ricerca per friendly name ed entity_id.
- Aggiunta migrazione iniziale delle associazioni Community già configurate.
- Dopo il primo salvataggio, le entità rimosse dalle stanze non vengono reinserite automaticamente.
- Aggiunto riconoscimento visuale dei dispositivi basato su nome visualizzato, friendly name, icona, device_class e dominio.
- Ampliati visual e icone per elettrodomestici, accessi, garage, clima, sensori, energia, EV/Wallbox e altri dispositivi.
- Nuova Panoramica V2 focalizzata su stati attivi, temperature, esterno/meteo, fotovoltaico/batteria e Wallbox/EV.
- Mantenute le 173 associazioni logiche Community.
- Aggiornato README con screenshot reali Casa V1 e Casa V2.
- Versione integrazione e frontend portata a **2.0.0**.

## 1.1.6
- Fixed room entity autocomplete binding.
- Existing configured Community mappings are migrated into their rooms when opening the configurator.
- Room suggestions now work immediately by friendly name or entity_id.


## 1.1.4 - 2026-08-17

- Stabilizzato il rendering delle card: niente più sfarfallii durante gli aggiornamenti di Home Assistant.
- Aggiunta ricerca delle entità anche per nome assegnato (`friendly_name`), oltre a entity_id e chiavi Community.
- I suggerimenti mostrano nome leggibile ed entity_id, salvando sempre l'entity_id reale.
- Applicata visibilità adattiva rigorosa a tutte le pagine: funzioni non configurate non generano più stati o fallback grafici.
- Nascosti automaticamente meteo, clima, finestre, tende, automazioni, sicurezza, energia e altri blocchi quando mancano le relative entità.
- Mantenute le 173 associazioni configurabili e la configurazione guidata in-dashboard.
- Rimossi artefatti `__pycache__` dal pacchetto di distribuzione.

## 1.1.3 - 2026-08-17

- aggiunta configurazione guidata delle 173 entità direttamente dalla dashboard;
- aggiunta ricerca delle funzioni e suggerimenti delle entity_id Home Assistant;
- salvataggio della configurazione tramite backend Community dedicato;
- entità, controlli e metriche non configurati vengono nascosti automaticamente;
- ambienti e voci di navigazione senza funzioni configurate vengono nascosti;
- aggiunte preview reali della Panoramica e del popup di configurazione nel README;
- mantenuto il file JSON separato come fallback/import-export;
- mantenuta la completa separazione dal domain personale `casa_dashboard`.


## 1.1.2 - 2026-08-17

- Rimossa dal repository la directory legacy `custom_components/casa_dashboard`.
- Il repository contiene ora una sola integrazione HACS: `custom_components/casa_dashboard_community`.
- Corretto definitivamente il percorso di installazione mostrato da HACS.
- Mantenuti domain, pannello, frontend e file entità dedicati alla Community.
- Confermate le 173 chiavi logiche configurabili e tutte le funzionalità della v1.1.1.

## 1.1.1 - 2026-08-17

- Correzione strutturale dell’installazione HACS: integrazione spostata definitivamente in `custom_components/casa_dashboard_community`.
- Domain dedicato `casa_dashboard_community`, separato dalla dashboard personale `casa_dashboard`.
- Pannello, static path, web component e file entità dedicati alla Community.
- La Community può ora convivere nella stessa istanza Home Assistant con la Casa Dashboard personale senza sovrascriverla.
- Confermate le 173 chiavi logiche configurabili e tutte le funzionalità introdotte nella v1.1.0.
- README aggiornato con pulsante **Add to HACS** e istruzioni di installazione corrette.

## 1.1.0 - 2026-08-17

- Portato nella Community il redesign premium/app-like della dashboard personale v4.2.9, mantenendo entità e versioning separati.
- Nuova Panoramica con hero/scena di casa e gerarchia visiva aggiornata.
- Migliorati avvisi porta d'ingresso, confronto comfort Cucina e composizione Camera.
- Aggiunte etichette umane per lux e radiazione solare, con formato compatto `klx`.
- Riorganizzata completamente la sezione meteo del Balcone.
- Aggiunta sezione opzionale Energia solare con FV, due canali/falde, casa, rete e batteria.
- Aggiunte 16 chiavi logiche `sensor.solar_*`; totale mappa entità: 173.
- Aggiunta migrazione non distruttiva del file `/config/www/casa-dashboard-community-entities.json`: le nuove chiavi vengono aggiunte senza sovrascrivere le associazioni esistenti.
- Migliorata la sezione Garage/Wallbox con potenza, carico contatore, energia sessione e limite ricarica in kW con A/V di dettaglio.
- Potenze FV/Wallbox normalizzate automaticamente da W o kW.
- Mantenuta la gestione sicura delle entità non configurate e il supporto tema chiaro/scuro.

## 1.0.0 - 2026-08-13

- Prima release pubblica di Casa Dashboard Community.
- Separata dal versioning della dashboard personale.
- Rimossi nomi personali e riferimenti specifici all'impianto originale.
- Introdotta la configurazione esterna delle entità tramite `/config/www/casa-dashboard-community-entities.json`.
- Aggiunta gestione sicura delle entità non configurate: stato `Non configurato` e comandi disabilitati.
- Mantenuti layout app-like, responsive desktop/mobile e supporto tema chiaro/scuro.
- Aggiunti `Realizzato da Fabio Vittori` e collegamento `☕ Offrimi un caffè` a Ko-fi.
- Aggiunta documentazione IT/EN e guida completa alla mappa entità.
