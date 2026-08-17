# 🏠 Casa Dashboard Community v1.1.2

Release correttiva per l’installazione tramite HACS.

## ✅ Correzione HACS

La vecchia directory `custom_components/casa_dashboard` è stata rimossa completamente dal repository.

Nel repository resta ora esclusivamente:

`custom_components/casa_dashboard_community`

HACS può quindi rilevare la Community Edition senza ambiguità e installarla nel percorso corretto:

`/config/custom_components/casa_dashboard_community`

## 🔀 Convivenza con Casa Dashboard personale

La Community continua a utilizzare:

- domain `casa_dashboard_community`
- pannello `casa-dashboard-community`
- frontend statico dedicato
- web component dedicato
- file entità `/config/www/casa-dashboard-community-entities.json`

Può quindi convivere con una dashboard personale basata su `casa_dashboard`.

## ✨ Funzionalità

Restano confermate tutte le funzionalità della v1.1.1 e le **173 associazioni logiche configurabili**.

## ☕ Supporta il progetto

https://ko-fi.com/fabvittori

---

**Realizzato da Fabio Vittori**
