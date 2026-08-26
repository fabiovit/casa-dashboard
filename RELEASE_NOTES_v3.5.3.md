# Casa Dashboard Community v3.5.3

## 🇬🇧 English

Hotfix for the image workflow after selecting a file.

- The configurator now preserves the scroll position after edits and when returning to a tab.

- Restored the **Add room** controls in the Rooms configurator.

- The selected photo is now compressed and shown immediately in the configurator.
- The image is stored in the configuration draft before backend file upload is attempted.
- Backend `/local/...` upload is now an optimization only: if it fails or times out, the selected image remains available.
- Added visible statuses for processing, acquired, verified and error states.
- Added upload and verification timeouts to avoid silent hangs.
- Inline fallback has been reduced to about 260 KB for safer configuration saves.

## 🇮🇹 Italiano

Hotfix dedicata al flusso dopo la selezione della foto.

- Il configuratore mantiene ora la posizione di scorrimento dopo le modifiche e quando si torna in una sezione.

- Ripristinati i pulsanti **Aggiungi stanza** nella pagina Stanze del configuratore.

- La foto selezionata viene ora compressa e mostrata immediatamente nel configuratore.
- L'immagine viene inserita nella configurazione temporanea prima di tentare il salvataggio backend.
- L'upload `/local/...` diventa un'ottimizzazione: se fallisce o va in timeout, la foto selezionata resta comunque disponibile.
- Aggiunti stati visibili per elaborazione, acquisizione, verifica ed errore.
- Aggiunti timeout per evitare blocchi silenziosi.
- Il fallback inline è stato ridotto a circa 260 KB per rendere più sicuro il salvataggio della configurazione.

**Realizzato da Fabio Vittori**
