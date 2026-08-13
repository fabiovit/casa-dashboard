# 🏠 Casa Dashboard Community

[![Release](https://img.shields.io/badge/release-v1.0.0-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Una dashboard app-like per **Home Assistant**, pensata per offrire una vista unica di casa senza dipendere dalle classiche card Lovelace.

La Community Edition nasce dalla dashboard personale di Fabio Vittori, ma è stata separata dalle entità private e resa configurabile per installazioni diverse.

**Realizzato da Fabio Vittori** · [☕ Offrimi un caffè](https://ko-fi.com/fabvittori)

## Versione

**v1.0.0 Community**

Questa è la prima release pubblica. Il ramo Community usa un versioning indipendente dalla dashboard personale da cui deriva il design.

## Caratteristiche

- Interfaccia custom, app-like e responsive.
- Desktop e smartphone con menu interno orizzontale e hamburger Home Assistant solo su mobile.
- Supporto ai temi chiaro/scuro di Home Assistant.
- Panoramica generale e sezioni Esterno, Scale, Ingresso, Cucina, Disimpegno, Bagno, Camera, Balcone e Garage.
- Sicurezza, luci, clima, tende, meteo, robot aspirapolvere, qualità aria, deumidificazione, EV e wallbox.
- Entità completamente separabili dall'interfaccia tramite file di configurazione esterno.
- Le entità non configurate vengono mostrate come **Non configurato** e i relativi comandi restano disabilitati.

## Installazione manuale

1. Copia `custom_components/casa_dashboard` in `/config/custom_components/`.
2. Riavvia Home Assistant.
3. Vai in **Impostazioni → Dispositivi e servizi → Aggiungi integrazione**.
4. Cerca **Casa Dashboard Community** e aggiungila.
5. Al primo avvio l’integrazione crea automaticamente `/config/www/casa-dashboard-entities.json`.
6. Apri quel file e inserisci le tue `entity_id` nella sezione `entities`.
7. Ricarica la pagina del browser/app. Per modifiche successive al file delle entità non serve riavviare Home Assistant.

> Le chiavi logiche a sinistra non devono essere rinominate. Inserisci soltanto la tua entity_id a destra. Puoi lasciare vuote le funzioni che non usi.

Consulta anche `examples/ENTITY_MAP.md` per l'elenco completo delle associazioni.

## HACS

Il repository è predisposto come custom integration. Dopo la pubblicazione del repository GitHub, può essere aggiunto a HACS come **Custom repository → Integration**.

## Configurazione delle entità

Esempio:

```json
{
  "entities": {
    "light.kitchen_main": "light.luce_cucina",
    "sensor.kitchen_temperature": "sensor.temperatura_cucina",
    "binary_sensor.entry_door": "binary_sensor.porta_ingresso"
  }
}
```

Il file personale resta in `/config/www/` e quindi non viene incluso negli aggiornamenti HACS della custom integration.

## Nota importante

Casa Dashboard Community è un **template avanzato**: case, stanze, dispositivi e automazioni cambiano da impianto a impianto. Alcune sezioni sono quindi opzionali e richiedono entità equivalenti alle funzioni mostrate.

La logica visuale dedicata a clima e tende è fornita come esempio e potrebbe non corrispondere alle automazioni del tuo impianto. Personalizzala prima di considerarla una rappresentazione affidabile delle tue automazioni.

## Supporto

Se il progetto ti piace e vuoi sostenerne lo sviluppo: **[☕ Offrimi un caffè su Ko-fi](https://ko-fi.com/fabvittori)**.

---

# English

**Casa Dashboard Community** is an app-like Home Assistant dashboard designed as a complete custom panel rather than a collection of standard Lovelace cards.

The Community Edition is based on Fabio Vittori's personal dashboard, with private entity IDs removed and a separate external entity mapping file for other Home Assistant installations.

**Created by Fabio Vittori** · [☕ Buy me a coffee](https://ko-fi.com/fabvittori)

On first setup the integration automatically creates `/config/www/casa-dashboard-entities.json`. Map the logical keys in that file to your real Home Assistant entity IDs. Empty entries are displayed as **Not configured** and their controls remain disabled.
