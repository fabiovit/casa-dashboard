# 🏠 Casa Dashboard Community

[![Release](https://img.shields.io/badge/release-v1.1.0-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Una dashboard app-like per **Home Assistant**, pensata per offrire una vista unica della casa senza dipendere dalle classiche card Lovelace.

La Community Edition nasce dalla dashboard personale di Fabio Vittori, ma mantiene **versioning, configurazione ed entity_id completamente separati** per poter essere adattata ad altre installazioni Home Assistant.

**Realizzato da Fabio Vittori** · [☕ Offrimi un caffè](https://ko-fi.com/fabvittori)

## Versione 1.1.0 Community

La **v1.1.0** porta nella versione pubblica il grande aggiornamento grafico e funzionale sviluppato sulla dashboard personale, mantenendo però la configurazione Community basata su chiavi logiche generiche.

### Novità principali

- redesign più profondo, premium e app-like;
- nuova Panoramica con hero/scena di casa e informazioni prioritarie;
- card e controlli ridisegnati con migliore gerarchia visiva;
- avvisi più evidenti per la porta d'ingresso;
- confronto comfort in Cucina più leggibile;
- ordine e composizione della sezione Camera aggiornati;
- luminosità espressa con etichette umane e formato compatto `klx`;
- radiazione solare con descrizione immediata dell'intensità;
- meteo Balcone completamente riorganizzato in blocchi tematici;
- nuova sezione opzionale **Energia solare** con FV, due falde/canali, casa, rete e batteria;
- SOC batteria sempre visibile e flussi carica/scarica più chiari;
- Garage/Wallbox aggiornato: potenza e limite ricarica in **kW**, A/V come dettaglio, carico contatore e sessione;
- supporto automatico a sensori di potenza esposti sia in W sia in kW;
- mappa esterna passata da **157 a 173 chiavi logiche**;
- aggiornamento non distruttivo del file entità: le nuove chiavi vengono aggiunte senza sovrascrivere quelle già configurate.

## Installazione manuale

1. Copia `custom_components/casa_dashboard` in `/config/custom_components/`.
2. Riavvia Home Assistant.
3. Vai in **Impostazioni → Dispositivi e servizi → Aggiungi integrazione**.
4. Cerca **Casa Dashboard Community** e aggiungila.
5. Al primo avvio viene creato automaticamente `/config/www/casa-dashboard-entities.json`.
6. Associa le chiavi logiche alle tue `entity_id` reali.
7. Ricarica la pagina del browser/app.

> Le chiavi logiche a sinistra non devono essere rinominate. Inserisci soltanto la tua entity_id a destra. Puoi lasciare vuote le funzioni che non usi.

Consulta `examples/ENTITY_MAP.md` per la mappa completa delle **173 associazioni**.

## Aggiornamento dalla v1.0.0

Installa la v1.1.0 e riavvia Home Assistant. L'integrazione controlla `/config/www/casa-dashboard-entities.json` e aggiunge soltanto le nuove chiavi mancanti, lasciando intatti i valori già associati.

Le 16 nuove chiavi `sensor.solar_*` sono opzionali: se non hai un impianto fotovoltaico puoi lasciarle vuote. L'intera sezione Energia solare resterà nascosta.

## HACS

Il repository è predisposto come custom integration e può essere aggiunto a HACS come **Custom repository → Integration**.

## Configurazione entità

Esempio:

```json
{
  "entities": {
    "light.kitchen_main": "light.luce_cucina",
    "sensor.kitchen_temperature": "sensor.temperatura_cucina",
    "binary_sensor.entry_door": "binary_sensor.porta_ingresso",
    "sensor.solar_pv_power": "sensor.tuo_fotovoltaico_potenza"
  }
}
```

Il file personale resta in `/config/www/` e non viene sovrascritto dagli aggiornamenti HACS.

### Fotovoltaico

Per il nuovo blocco Energia solare sono disponibili 16 chiavi generiche `sensor.solar_*`. Le potenze possono essere in **W o kW**. Per la convenzione dei segni di rete e batteria consulta `examples/ENTITY_MAP.md`.

## Nota importante

Casa Dashboard Community è un **template avanzato**: stanze, dispositivi, automazioni e sensori cambiano da impianto a impianto. Le funzioni non utilizzate possono restare non configurate.

Le logiche visuali dedicate a clima, tende, meteo ed energia sono esempi generici e devono essere adattate alla logica reale del proprio impianto prima di essere considerate una rappresentazione affidabile delle automazioni.

## Supporto

Se il progetto ti piace e vuoi sostenerne lo sviluppo: **[☕ Offrimi un caffè su Ko-fi](https://ko-fi.com/fabvittori)**.

---

# English

**Casa Dashboard Community** is an app-like Home Assistant dashboard built as a complete custom panel rather than a collection of standard Lovelace cards.

Version **1.1.0** brings the new premium visual design, improved weather/room layouts, optional photovoltaic and battery visualization, and updated EV/wallbox metrics. The external mapping now exposes **173 logical entity keys** while keeping private Home Assistant entity IDs outside the integration.

When upgrading from v1.0.0, missing mapping keys are added automatically without overwriting existing user assignments.

**Created by Fabio Vittori** · [☕ Buy me a coffee](https://ko-fi.com/fabvittori)
