# Changelog

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
