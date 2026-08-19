# 🏠 Casa Dashboard Community

[🇬🇧 English](README.md) | 🇮🇹 **Italiano**

[![Release](https://img.shields.io/badge/release-v2.1.0-blue)](https://github.com/fabiovit/casa-dashboard/releases)
[![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz/)
[![Validate](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hacs.yml?branch=main&label=Validate)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hacs.yml)
[![Hassfest](https://img.shields.io/github/actions/workflow/status/fabiovit/casa-dashboard/hassfest.yml?branch=main&label=Hassfest)](https://github.com/fabiovit/casa-dashboard/actions/workflows/hassfest.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Add to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fabiovit&repository=casa-dashboard&category=integration)

Casa Dashboard Community è una dashboard app-like per **Home Assistant**, realizzata come pannello custom completo e pensata per adattarsi a installazioni molto diverse senza dipendere dalle classiche card Lovelace.

**Casa Dashboard Community v2.1.0** include due esperienze grafiche, **Casa V1** e **Casa V2**, stanze dinamiche, configurazione delle entità direttamente dalla dashboard e supporto nativo **Italiano / Inglese**.

La Community Edition usa il domain tecnico `casa_dashboard_community`, il pannello `casa-dashboard-community` e il file dedicato `/config/www/casa-dashboard-community-entities.json`, così può convivere con altre installazioni Casa Dashboard senza sovrascriverle.

**Realizzato da Fabio Vittori** · [☕ Offrimi un caffè](https://ko-fi.com/fabvittori)

# 🚀 Versione 2.1.0

La versione 2.1.0 introduce il supporto nativo **Italiano / Inglese** direttamente all'interno della dashboard.

È possibile cambiare la lingua dell'interfaccia tra:

- 🇮🇹 Italiano
- 🇬🇧 English

La lingua selezionata viene ricordata sul browser/dispositivo utilizzato.

I nomi personalizzati delle stanze e i nomi delle entità Home Assistant rimangono esattamente quelli configurati dall'utente.

## ✨ Casa V1 + Casa V2

### Casa V1 — Classic

La grafica originale della Community resta disponibile per chi preferisce l'esperienza classica della serie 1.x.

![Casa Dashboard Community - Casa V1 Classic](images/casa-v1-classic.png)

### Casa V2 — Dynamic

Casa V2 introduce un'esperienza più visuale con scene dedicate agli ambienti, dispositivi contestualizzati e una Panoramica concentrata sulle informazioni realmente importanti.

> Gli screenshot V2 mostrano un'installazione di esempio. Fotovoltaico, EV, Wallbox e altri dispositivi sono opzionali e vengono visualizzati solo quando configurati.

#### Panoramica V2

![Casa Dashboard Community - Casa V2 Panoramica](images/casa-v2-overview.png)

#### Ingresso V2

![Casa Dashboard Community - Casa V2 Ingresso](images/casa-v2-ingresso.png)

#### Garage V2

![Casa Dashboard Community - Casa V2 Garage](images/casa-v2-garage.png)

## 🏠 Stanze dinamiche

Con Casa V2 gli ambienti non sono più vincolati alla struttura della casa originale.

È possibile:

- creare nuove stanze;
- assegnare liberamente il nome;
- scegliere il tipo di ambiente;
- scegliere l'icona;
- riordinare gli ambienti;
- eliminare quelli non utilizzati;
- creare più stanze dello stesso tipo;
- associare più entità Home Assistant alla stessa stanza.

Sono previsti tipi visuali per Cucina, Bagno, Camera, Soggiorno, Studio, Lavanderia, Taverna, Garage, Balcone/Terrazzo, Esterno, Scale, Ingresso, Disimpegno e ambiente generico.

## ⚙️ Configuratore evoluto

La configurazione avviene direttamente dalla dashboard tramite **Configura**.

Le entità possono essere cercate usando:

- il nome assegnato in Home Assistant (`friendly_name`);
- l'`entity_id`;
- il nome visualizzato scelto nella dashboard.

Le associazioni Community esistenti vengono importate nelle stanze durante la prima configurazione. Dopo il primo salvataggio, la sezione Stanze diventa la fonte ufficiale: un'entità rimossa manualmente da una stanza non viene reinserita automaticamente.

Il configuratore mantiene anche le **173 associazioni logiche Community** utilizzate dalle funzioni globali e specialistiche.

## 🏷️ Riconoscimento intelligente dei dispositivi

Casa V2 utilizza più informazioni per scegliere automaticamente icona e visual più appropriati:

1. nome visualizzato;
2. friendly name Home Assistant;
3. funzione riconosciuta;
4. icona Home Assistant;
5. `device_class`;
6. dominio dell'entità.

Questo consente, ad esempio, di visualizzare correttamente una **Friggitrice** anche quando l'entità reale è una smart plug con un nome tecnico generico.

Sono gestite numerose categorie, tra cui luci, LED, prese, friggitrice, Bimby/blender, forno, microonde, lavastoviglie, lavatrice, asciugatrice, TV, climatizzazione, purificatori, deumidificatori, cancelli, portoncini, basculanti, tende, tapparelle, robot, irrigazione, tagliaerba, allarme, sensori ambientali, Wallbox/EV, fotovoltaico, inverter e batterie.

## 📊 Panoramica V2

La nuova Panoramica evita di duplicare l'elenco degli ambienti e mette in evidenza:

- stati attivi;
- temperature principali;
- condizioni esterne e meteo;
- fotovoltaico e batteria;
- Wallbox e veicolo elettrico.

Le sezioni senza entità utili restano nascoste.

## 🌍 Lingue

L'interfaccia della dashboard può ora essere cambiata tra:

- 🇮🇹 Italiano
- 🇬🇧 English

Il selettore lingua è disponibile direttamente nell'header della dashboard.

Il sistema di traduzione copre Casa V1, Casa V2, Panoramica, stanze dinamiche, configuratore, pagina Informazioni e i principali stati/controlli.

I nomi delle entità Home Assistant e i nomi personalizzati delle stanze vengono volutamente mantenuti.

## 🔄 Migrazione dalla serie 1.x

L'aggiornamento mantiene separata la configurazione Community.

Al primo utilizzo del nuovo gestore Stanze, le associazioni Community esistenti vengono utilizzate per inizializzare gli ambienti compatibili. Dopo il salvataggio, le stanze vengono gestite direttamente dalla nuova configurazione.

**Casa V1 non viene rimossa:** resta selezionabile insieme a Casa V2.

## 📱 Responsive

Entrambe le esperienze sono progettate per desktop e smartphone con menu e layout adattivi.

## 📦 Installazione HACS

1. Apri **HACS**.
2. Aggiungi `https://github.com/fabiovit/casa-dashboard` come repository personalizzato di tipo **Integrazione**, oppure usa il pulsante **Add to HACS** in alto.
3. Installa **Casa Dashboard Community**.
4. Riavvia Home Assistant.
5. Vai in **Impostazioni → Dispositivi e servizi → Aggiungi integrazione**.
6. Cerca **Casa Dashboard Community**.
7. Apri la dashboard e premi **Configura**.

## 📦 Installazione manuale

1. Copia `custom_components/casa_dashboard_community` in `/config/custom_components/`.
2. Riavvia Home Assistant.
3. Aggiungi **Casa Dashboard Community** da **Impostazioni → Dispositivi e servizi**.
4. Apri la dashboard e configura stanze ed entità.

## ℹ️ Nota

Casa Dashboard Community è un **template avanzato**. Ogni installazione Home Assistant è diversa: dispositivi, sensori, automazioni, fotovoltaico, EV e Wallbox sono opzionali.

Le funzioni non configurate non vengono mostrate.

## ☕ Supporto

Se il progetto ti piace e vuoi sostenerne lo sviluppo: **[Offrimi un caffè su Ko-fi](https://ko-fi.com/fabvittori)**.
