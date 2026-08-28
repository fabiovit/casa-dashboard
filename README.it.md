# 🏠 Casa Dashboard Community

[🇬🇧 English](README.md) | 🇮🇹 **Italiano**

[![Release](https://img.shields.io/badge/release-v4.0.0-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Add to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fabiovit&repository=casa-dashboard&category=integration)

Casa Dashboard Community è una dashboard app-like completa per **Home Assistant**, pensata per adattarsi ad abitazioni diverse senza dipendere dalle classiche card Lovelace.

La **v4.0.0** consolida l'attuale generazione Dynamic in una base stabile e più ordinata, con versioning allineato tra frontend e backend.

**Realizzato da Fabio Vittori** · [☕ Offrimi un caffè](https://ko-fi.com/fabvittori)

## 🖼️ Casa Dashboard Community 4.0

La 4.0 porta una nuova esperienza visiva coerente in **tema scuro e chiaro**, mantenendo la stessa struttura dinamica in ogni stanza.

### Panoramica

![Casa Dashboard Community 4.0 - Panoramica tema scuro](images/casa-v4-overview-dark.png)

![Casa Dashboard Community 4.0 - Panoramica tema chiaro](images/casa-v4-overview-light.png)

### Ingresso

![Casa Dashboard Community 4.0 - Ingresso tema scuro](images/casa-v4-ingresso-dark.png)

![Casa Dashboard Community 4.0 - Ingresso tema chiaro](images/casa-v4-ingresso-light.png)

### Cucina

![Casa Dashboard Community 4.0 - Cucina tema scuro](images/casa-v4-cucina-dark.png)

![Casa Dashboard Community 4.0 - Cucina tema chiaro](images/casa-v4-cucina-light.png)

### Balcone

![Casa Dashboard Community 4.0 - Balcone tema scuro](images/casa-v4-balcone-dark.png)

![Casa Dashboard Community 4.0 - Balcone tema chiaro](images/casa-v4-balcone-light.png)

### Garage, EV e Wallbox

![Casa Dashboard Community 4.0 - Garage tema scuro](images/casa-v4-garage-dark.png)

![Casa Dashboard Community 4.0 - Garage tema chiaro](images/casa-v4-garage-light.png)

### Configuratore

![Casa Dashboard Community 4.0 - Configuratore Panoramica](images/casa-v4-config-overview.png)

![Casa Dashboard Community 4.0 - Configuratore Stanze](images/casa-v4-config-rooms.png)

![Casa Dashboard Community 4.0 - Configuratore Energia e Mobilità](images/casa-v4-config-energy.png)

## 🛡️ Sicurezza e accesso

Le stanze dinamiche riconoscono le entità `lock.*` e `alarm_control_panel.*` e, quando configurate, possono mostrare comandi dedicati per serratura e antifurto.

## ☀️ Visual Energia Avanzato

Casa Dashboard 4.0 supporta le modalità Fotovoltaico **Compatta** e **Avanzata**, con produzione live, eventuali PV1/PV2, SOC e flusso batteria e nodi Casa / Inverter / Batteria / Rete.

Le convenzioni del segno di Rete e Batteria sono configurabili per adattarsi a integrazioni inverter differenti.

## 🔗 Moduli condivisi nelle stanze

Configura i dati globali una sola volta e richiamali nelle stanze senza duplicare le associazioni:

- Energia solare
- EV + Wallbox
- Meteo
- Allarme

## 🧭 Configuratore a pagine

Il configuratore è suddiviso in pagine dedicate:

- Panoramica
- Stanze
- Dispositivi
- Energia & Mobilità
- Meteo & Sicurezza
- Avanzate

## 🎨 Personalizzazione visuale

Puoi personalizzare le label della Panoramica, i nomi di auto e Wallbox, le immagini delle stanze, i nomi visualizzati, le icone e le foto degli oggetti.

Le foto caricate per le entità vengono ridimensionate e salvate sotto `/local/casa_dashboard_community/uploads/`.

## 🏠 Stanze dinamiche

Casa Dashboard 4.0 permette di creare, rinominare, riordinare e rimuovere stanze, scegliere tipo/icona e associare più entità Home Assistant alla stessa stanza.

## ⚙️ Configuratore visuale

Le entità possono essere cercate tramite friendly name Home Assistant, `entity_id` o nome visualizzato personalizzato. Le installazioni grandi sono supportate con pagine raggruppate e scroll dedicati.

## 🧠 Riconoscimento intelligente

Casa Dashboard può scegliere un visual adatto usando nome personalizzato, friendly name Home Assistant, funzione riconosciuta, icona HA, `device_class` e dominio dell'entità.

## 📊 Panoramica

La Panoramica mette in evidenza stati attivi, temperature, meteo, fotovoltaico/batteria, rete, Wallbox e, se configurati, i dati reali dell'auto elettrica. Le sezioni non configurate restano nascoste.

## 🌍 Lingue

Supporto nativo:

- 🇮🇹 Italiano
- 🇬🇧 English

La lingua scelta viene memorizzata localmente. I nomi personalizzati delle stanze e delle entità Home Assistant vengono mantenuti.

## 📱 Responsive

Casa Dashboard 4.0 è progettata per desktop e smartphone.

## 📦 Installazione HACS

1. Apri **HACS**.
2. Aggiungi `https://github.com/fabiovit/casa-dashboard` come repository personalizzato di tipo **Integrazione**, oppure usa il pulsante **Add to HACS** qui sopra.
3. Installa **Casa Dashboard Community**.
4. Riavvia Home Assistant.
5. Vai in **Impostazioni → Dispositivi e servizi → Aggiungi integrazione**.
6. Cerca **Casa Dashboard Community**.
7. Apri il nuovo pannello laterale e premi **Configura**.

## 📦 Installazione manuale

Copia `custom_components/casa_dashboard_community` in `/config/custom_components/`, riavvia Home Assistant e aggiungi l'integrazione da **Impostazioni → Dispositivi e servizi**.

## ℹ️ Note

Dispositivi, sensori, automazioni, fotovoltaico, EV e Wallbox sono opzionali. Le funzioni non configurate vengono nascoste automaticamente.

## ☕ Supporto

Se il progetto ti piace: **[Offrimi un caffè su Ko-fi](https://ko-fi.com/fabvittori)**.
