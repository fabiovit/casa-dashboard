# Casa Dashboard Community v3.0.1

## 🇬🇧 English

This hotfix resolves an installation / first-configuration error reported on Home Assistant 2025.9.3.

### Fixed

- Removed dependency on `frontend.async_panel_exists`, which is not available in every Home Assistant frontend version.
- Panel registration now checks Home Assistant's registered frontend panel mapping directly.
- The same compatibility logic is used when unloading/reloading the integration.
- Existing Casa Dashboard configuration and room/entity mappings are preserved.

Users affected by the error below should update to v3.0.1:

`AttributeError: module 'homeassistant.components.frontend' has no attribute 'async_panel_exists'`

---

## 🇮🇹 Italiano

Questa hotfix risolve un errore di installazione / prima configurazione segnalato su Home Assistant 2025.9.3.

### Correzioni

- Rimossa la dipendenza da `frontend.async_panel_exists`, non disponibile in tutte le versioni frontend di Home Assistant.
- La registrazione del pannello verifica ora direttamente il registro dei pannelli frontend di Home Assistant.
- La stessa logica di compatibilità viene utilizzata durante unload/reload dell'integrazione.
- Configurazione, stanze e associazioni entità esistenti vengono mantenute.

Gli utenti che ricevono l'errore seguente devono aggiornare alla v3.0.1:

`AttributeError: module 'homeassistant.components.frontend' has no attribute 'async_panel_exists'`

**Realizzato da Fabio Vittori**
