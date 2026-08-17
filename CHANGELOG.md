# Changelog

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
