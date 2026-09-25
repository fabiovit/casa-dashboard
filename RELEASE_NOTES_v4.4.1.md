# Casa Dashboard Community v4.4.1

## 🇮🇹 Italiano

### Correzioni
- Corretto lo stato dei sensori di perdita acqua: **Asciutto / Bagnato** anziché `Spento` o `—`.
- Uniformata la lettura dei sensori `binary_sensor` con classe `moisture` e dei rilevatori di perdita acqua riconosciuti dalla dashboard.
- Corretto il renderer grafico Umidità, che tentava di interpretare come percentuale uno stato binario; i normali sensori di umidità numerica mantengono la visualizzazione in `%`.
- Gestiti anche gli stati non disponibili e sconosciuti.

### Ringraziamenti
Un ringraziamento speciale a **Mario Pagano** per i test su desktop e smartphone e per aver verificato la correzione.

## 🇬🇧 English

### Fixes
- Fixed water-leak sensor status: **Dry / Wet** instead of `Off` or `—`.
- Unified handling of `binary_sensor` entities with the `moisture` device class and water-leak detectors recognized by the dashboard.
- Fixed the Humidity visual renderer, which previously treated a binary state as a numeric percentage; regular numeric humidity sensors still display `%`.
- Handled unavailable and unknown states.

### Acknowledgements
Special thanks to **Mario Pagano** for desktop and mobile testing and for verifying the fix.

---
**Realizzato da Fabio Vittori · Created by Fabio Vittori**
