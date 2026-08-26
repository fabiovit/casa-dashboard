# Casa Dashboard Community v3.5.1

## 🇬🇧 English
Maintenance release fixing custom image upload and persistence.

- Room and per-object images are now retained reliably.
- Uploaded images show an immediate preview in the configurator.
- Casa Dashboard first stores images under `/config/www/casa_dashboard_community/uploads/`.
- If the upload WebSocket command is not available yet, a compressed inline image is stored safely in the Community configuration instead.
- Improved WebSocket registration for config-entry installations.
- Fixed configurator radio/select persistence.
- All v3.5.0 Advanced Energy View features remain unchanged.

## 🇮🇹 Italiano
Release di manutenzione che corregge caricamento e persistenza delle immagini personalizzate.

- Le foto di stanze e singoli oggetti vengono ora mantenute correttamente.
- Il configuratore mostra subito un'anteprima della foto caricata.
- Casa Dashboard prova prima a salvare le immagini in `/config/www/casa_dashboard_community/uploads/`.
- Se il comando WebSocket di upload non è ancora disponibile, viene salvata automaticamente una versione compressa direttamente nella configurazione Community.
- Migliorata la registrazione WebSocket nelle installazioni tramite config entry.
- Corretta la persistenza di selettori/radio del configuratore.
- Tutte le funzioni Advanced Energy View della v3.5.0 rimangono invariate.

**Realizzato da Fabio Vittori**
