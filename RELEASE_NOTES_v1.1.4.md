# 🏠 Casa Dashboard Community v1.1.4

Release stabile di **Casa Dashboard Community** per Home Assistant.

Questa versione consolida il nuovo configuratore integrato e include gli ultimi affinamenti verificati direttamente in Home Assistant.

## ✨ Novità e correzioni

- configurazione guidata delle **173 associazioni logiche** direttamente dalla dashboard;
- ricerca delle entità anche tramite **nome assegnato / friendly name**;
- suggerimenti leggibili con nome entità + `entity_id`;
- eliminato lo sfarfallio delle card durante gli aggiornamenti di Home Assistant;
- rendering ottimizzato: la pagina viene ridisegnata solo quando cambia davvero una delle entità configurate;
- visibilità adattiva estesa a tutte le pagine;
- card, metriche, automazioni e sezioni non configurate restano nascoste;
- eliminati i falsi stati di fallback come “Asciutto”, “Nessuno”, “Spento” o “Chiuso” quando manca la relativa entità;
- mantenuta la separazione completa dal progetto personale tramite `casa_dashboard_community`;
- rimossi artefatti `__pycache__` dal pacchetto.

## ⚙️ Configurazione

Premi **Configura** nella dashboard per aprire il popup di associazione delle entità. Puoi cercare per stanza, funzione, chiave, `entity_id` o nome assegnato in Home Assistant.

Le funzioni lasciate vuote non vengono mostrate nella dashboard.

La configurazione viene salvata separatamente in:

`/config/www/casa-dashboard-community-entities.json`

## 🔄 Aggiornamento

Dopo l'aggiornamento tramite HACS, **riavvia Home Assistant** prima di utilizzare il configuratore o il pannello aggiornato.

## ☕ Supporta il progetto

https://ko-fi.com/fabvittori

---

**Realizzato da Fabio Vittori**
