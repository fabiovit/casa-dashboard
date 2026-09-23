# Casa Dashboard Community v4.3.1

La v4.3.1 consolida il lavoro di rifinitura e test della Casa Dashboard Community su desktop e smartphone.

## Novità principali

- **Plance Home Assistant**: Casa Dashboard Community compare tra le dashboard di Home Assistant e può essere scelta come dashboard predefinita per dispositivo/app.
- **Icone luci**: le icone personalizzate delle entità `light.*` mostrano correttamente lo stato acceso in Automatico, Compatta, Normale, Larga e Intera.
- **Smart Lock**: card allineata al sistema di dimensionamento standard delle altre entità, con resa più coerente su desktop e smartphone.
- **Fotovoltaico**: ulteriori rifiniture al layout compatto desktop e alla batteria/SOC su smartphone per evitare overflow.
- **Stanze e dispositivi**: intestazioni, contrasto, ordinamento, anteprime e leggibilità ulteriormente stabilizzati.
- **Responsive**: mantenuta la geometria approvata su PC e smartphone senza reintrodurre override globali invasivi.

## Nota sulle dimensioni

Le modalità **Compatta** e **Normale** restano liberamente selezionabili. Per entità con molte informazioni o numerosi comandi può essere preferibile usare **Automatico**, **Larga** o **Intera**.

## Aggiornamento

Dopo l'aggiornamento è consigliato un riavvio completo di Home Assistant, necessario in particolare per la registrazione della dashboard tra le Plance.

Realizzato da Fabio Vittori.
