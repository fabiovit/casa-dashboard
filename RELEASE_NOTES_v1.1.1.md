# 🏠 Casa Dashboard Community v1.1.1

Release correttiva importante per **Casa Dashboard Community**.

Questa versione risolve il conflitto di installazione con la Casa Dashboard personale: la Community Edition utilizza ora definitivamente un’integrazione, un domain e percorsi dedicati.

## 🔀 Community completamente separata

La Community viene installata in:

`/config/custom_components/casa_dashboard_community`

con domain:

`casa_dashboard_community`

Utilizza inoltre:

- pannello dedicato `casa-dashboard-community`;
- static path frontend dedicato;
- web component dedicato;
- file entità `/config/www/casa-dashboard-community-entities.json`.

In questo modo può convivere nella stessa istanza Home Assistant con una Casa Dashboard personale basata su `casa_dashboard`, senza sovrascriverla.

## ✨ Funzionalità

Restano incluse tutte le novità della v1.1.0:

- interfaccia app-like responsive desktop e smartphone;
- supporto tema chiaro e scuro;
- Casa, Garage, Meteo, Energia e Wallbox;
- sicurezza, luci, clima e serramenti;
- fotovoltaico e batteria opzionali;
- EV e ricarica;
- **173 associazioni logiche configurabili**;
- configurazione delle entity_id separata dal frontend.

## 🧩 HACS

Il README include il pulsante **Add to HACS** per aggiungere rapidamente il repository come integrazione personalizzata.

Dopo l’installazione e il riavvio di Home Assistant, aggiungi **Casa Dashboard Community** da **Impostazioni → Dispositivi e servizi**.

## ⚠️ Nota per chi aveva installato la precedente Community

La precedente build poteva essere proposta da HACS nella cartella `custom_components/casa_dashboard`. La v1.1.1 corregge definitivamente questo comportamento.

Il file entità della Community è ora:

`/config/www/casa-dashboard-community-entities.json`

Non viene effettuata alcuna copia automatica dal file della dashboard personale, per evitare collisioni o importazioni involontarie.

## ☕ Supporta il progetto

Se Casa Dashboard Community ti piace e vuoi supportarne lo sviluppo:

https://ko-fi.com/fabvittori

---

**Realizzato da Fabio Vittori**
