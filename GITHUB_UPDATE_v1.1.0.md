# Aggiornamento GitHub – Casa Dashboard Community v1.1.0

Questa cartella contiene i file del repository pubblico **fabiovit/casa-dashboard** aggiornati alla v1.1.0.

## 1. Aggiorna i file del repository

Estrai lo ZIP e carica su GitHub **il contenuto della cartella**, non il file ZIP come sorgente del repository.

Sostituisci/aggiorna i file esistenti mantenendo la stessa struttura, in particolare:

- `custom_components/casa_dashboard/`
- `.github/workflows/`
- `examples/`
- `README.md`
- `CHANGELOG.md`
- `hacs.json`
- `LICENSE`

Sono stati aggiunti anche:

- `RELEASE_NOTES_v1.1.0.md`
- questo file `GITHUB_UPDATE_v1.1.0.md`
- nuovi frammenti frontend fino a `casa-dashboard-panel.part14.txt`

Commit suggerito:

`Release Casa Dashboard Community v1.1.0`

## 2. Controlla GitHub Actions

Dopo il commit apri **Actions** e attendi che risultino verdi:

- `HACS validation`
- `Hassfest`

Non creare la release finché entrambi non sono verdi.

## 3. Crea la release

Vai in **Releases → Draft a new release**.

Imposta:

- **Tag:** `v1.1.0`
- **Target:** `main`
- **Release title:** `Casa Dashboard Community v1.1.0`
- **Set as the latest release:** attivo
- **Pre-release:** disattivo

Nel testo della release incolla il contenuto di `RELEASE_NOTES_v1.1.0.md`.

## 4. Verifica badge README

Dopo la pubblicazione controlla che in testa al README compaiano:

- release `v1.1.0`
- HACS Custom
- Validate passing
- Hassfest passing
- license MIT

## 5. Test aggiornamento Home Assistant

Per un'installazione già su v1.0.0:

1. aggiorna la custom integration;
2. riavvia Home Assistant;
3. controlla `/config/www/casa-dashboard-entities.json`;
4. le vecchie associazioni devono essere ancora presenti;
5. in fondo alla mappa devono comparire anche le nuove chiavi `sensor.solar_*` non configurate.

Se non si usa il fotovoltaico, le nuove chiavi possono restare vuote: la sezione Energia solare resterà nascosta.

## Testo breve per il commit

`Release Casa Dashboard Community v1.1.0`

## Testo breve per la descrizione release

Usa integralmente `RELEASE_NOTES_v1.1.0.md`.
