# 🏠 Casa Dashboard Community v1.1.0

Seconda release pubblica di **Casa Dashboard Community** per Home Assistant.

La v1.1.0 porta nella Community il grande aggiornamento grafico e funzionale sviluppato sulla dashboard personale, mantenendo completamente separati entity_id, configurazione e versioning.

## ✨ Novità

- nuovo redesign premium e ancora più app-like;
- Panoramica ridisegnata con hero/scena di casa;
- card, controlli e gerarchie visive rinnovate;
- avvisi porta d'ingresso più evidenti;
- confronto comfort Cucina migliorato;
- sezione Camera riorganizzata;
- lux con descrizioni umane e formato compatto `klx`;
- radiazione solare con indicazione immediata dell'intensità;
- meteo Balcone completamente riorganizzato;
- nuova sezione opzionale **Energia solare**;
- visualizzazione FV totale, due falde/canali, consumo casa, rete e batteria;
- SOC batteria sempre visibile e stato carica/scarica più chiaro;
- Garage/Wallbox con potenza, carico contatore, energia sessione e limite ricarica in kW;
- A/V mantenuti come dettaglio diagnostico;
- supporto automatico a sensori di potenza in W o kW.

## ⚙️ Entità configurabili

La mappa passa da **157 a 173 chiavi logiche**.

Sono state aggiunte 16 nuove chiavi generiche `sensor.solar_*` dedicate a fotovoltaico e batteria.

La sezione Energia solare è opzionale: se `sensor.solar_pv_power` non viene configurato, il blocco non appare.

### Aggiornamento dalla v1.0.0

Dopo l'installazione della v1.1.0 e il riavvio di Home Assistant, l'integrazione aggiunge automaticamente al file:

`/config/www/casa-dashboard-entities.json`

le nuove chiavi mancanti, **senza modificare o sovrascrivere le associazioni già presenti**.

## ✅ Validazione

La release mantiene i workflow dedicati a:

- HACS validation
- Hassfest

## ☕ Supporta il progetto

Se Casa Dashboard ti piace e vuoi supportarne lo sviluppo:

https://ko-fi.com/fabvittori

---

**Realizzato da Fabio Vittori**
