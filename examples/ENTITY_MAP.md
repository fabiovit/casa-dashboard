# Mappa entità – Casa Dashboard Community

Compila `entities` nel file `/config/www/casa-dashboard-community-entities.json`. Le chiavi a sinistra **non vanno cambiate**: a destra inserisci la tua `entity_id` reale. Le voci lasciate vuote vengono mostrate come **Non configurato** e i relativi comandi sono disabilitati.

Dalla **v1.1.0** la mappa contiene **173 chiavi logiche**. Se aggiorni dalla v1.0.0, al riavvio Home Assistant aggiunge automaticamente le nuove chiavi mancanti senza modificare le associazioni già configurate.

## Sicurezza e accessi

- `alarm_control_panel.home_alarm`
- `binary_sensor.entry_door`
- `binary_sensor.entry_motion`
- `binary_sensor.entry_occupancy`
- `binary_sensor.garage_door_contact`
- `input_boolean.entry_door_unlock`
- `input_boolean.main_gate`
- `input_boolean.pedestrian_gate`
- `switch.garage_door_command`
- `switch.gate_command`

## Luci

- `light.balcony_bedroom`
- `light.balcony_kitchen`
- `light.bathroom_cabinet`
- `light.bathroom_main`
- `light.bedroom_lamp_1`
- `light.bedroom_lamp_2`
- `light.bedroom_led`
- `light.bedroom_main`
- `light.entry_main`
- `light.garage_1`
- `light.garage_2`
- `light.garage_air_purifier_backlight`
- `light.hallway_main`
- `light.kitchen_led`
- `light.kitchen_main`
- `light.living_tv_led`
- `light.stairs`

## Cucina

- `binary_sensor.kitchen_cabinet_door`
- `binary_sensor.kitchen_door_window`
- `binary_sensor.kitchen_motion`
- `binary_sensor.kitchen_occupancy`
- `binary_sensor.kitchen_window_vibration`
- `climate.kitchen`
- `cover.kitchen_blind`
- `input_boolean.kitchen_climate_manual`
- `sensor.kitchen_climate_temperature`
- `sensor.kitchen_humidity`
- `sensor.kitchen_illuminance`
- `sensor.kitchen_temperature`
- `switch.kitchen_appliance_1`
- `switch.kitchen_appliance_2`
- `switch.kitchen_hood`
- `switch.kitchen_tv`

## Bagno

- `binary_sensor.bathroom_cabinet_door`
- `binary_sensor.bathroom_motion`
- `binary_sensor.bathroom_occupancy`
- `binary_sensor.bathroom_water_leak`
- `binary_sensor.bathroom_window`
- `binary_sensor.bathroom_window_vibration`
- `cover.bathroom_blind`
- `fan.bathroom_extractor`
- `input_boolean.bathroom_custom_mode`
- `script.bathroom_custom_action`
- `sensor.bathroom_humidity`
- `sensor.bathroom_illuminance`
- `sensor.bathroom_temperature`

## Camera

- `binary_sensor.bedroom_door_window`
- `binary_sensor.bedroom_window`
- `binary_sensor.bedroom_window_vibration`
- `climate.bedroom`
- `cover.bedroom_blind`
- `input_boolean.bedroom_climate_manual`
- `sensor.bedroom_climate_temperature`
- `sensor.bedroom_humidity`
- `sensor.bedroom_temperature`
- `switch.bedroom_tv`

## Disimpegno

- `binary_sensor.hallway_motion`
- `binary_sensor.hallway_occupancy`
- `sensor.hallway_illuminance`

## Balcone e meteo

- `binary_sensor.balcony_motion`
- `binary_sensor.balcony_occupancy`
- `binary_sensor.balcony_water`
- `binary_sensor.weather_rain`
- `binary_sensor.weather_storm_alert`
- `cover.balcony_bedroom_blind`
- `cover.balcony_kitchen_blind`
- `input_boolean.blinds_manual_mode`
- `input_datetime.blinds_last_wind_raise`
- `sensor.weather_absolute_pressure`
- `sensor.weather_dewpoint`
- `sensor.weather_feels_like_temperature`
- `sensor.weather_indoor_dewpoint`
- `sensor.weather_indoor_humidity`
- `sensor.weather_indoor_temperature`
- `sensor.weather_lightning_azimuth`
- `sensor.weather_lightning_count`
- `sensor.weather_lightning_distance`
- `sensor.weather_max_daily_gust`
- `sensor.weather_outdoor_humidity`
- `sensor.weather_outdoor_temperature`
- `sensor.weather_rain_24h`
- `sensor.weather_rain_daily`
- `sensor.weather_rain_event`
- `sensor.weather_rain_hourly`
- `sensor.weather_rain_monthly`
- `sensor.weather_rain_rate`
- `sensor.weather_rain_weekly`
- `sensor.weather_rain_yearly`
- `sensor.weather_relative_pressure`
- `sensor.weather_solar_lux`
- `sensor.weather_solar_radiation`
- `sensor.weather_uv_index`
- `sensor.weather_vpd`
- `sensor.weather_wind_chill`
- `sensor.weather_wind_direction`
- `sensor.weather_wind_direction_10m`
- `sensor.weather_wind_gust`
- `sensor.weather_wind_speed`
- `switch.balcony_barbecue`

## Fotovoltaico e batteria – nuovo in v1.1.0

Questa sezione è **opzionale**. Se `sensor.solar_pv_power` resta vuoto, il blocco Energia solare non viene mostrato.

- `sensor.solar_pv_power` — produzione FV totale istantanea
- `sensor.solar_pv1_power` — potenza falda/canale FV 1
- `sensor.solar_pv1_voltage` — tensione FV 1
- `sensor.solar_pv1_current` — corrente FV 1
- `sensor.solar_pv2_power` — potenza falda/canale FV 2
- `sensor.solar_pv2_voltage` — tensione FV 2
- `sensor.solar_pv2_current` — corrente FV 2
- `sensor.solar_energy_today` — energia prodotta oggi
- `sensor.solar_load_power` — consumo istantaneo casa
- `sensor.solar_grid_power` — scambio rete
- `sensor.solar_battery_soc` — stato di carica batteria
- `sensor.solar_battery_power` — potenza batteria
- `sensor.solar_battery_mode` — stato/modalità batteria
- `sensor.solar_battery_charged_today` — energia caricata oggi
- `sensor.solar_battery_discharged_today` — energia scaricata oggi
- `sensor.solar_battery_losses_today` — perdite batteria oggi

### Convenzioni energia

- Le potenze possono essere esposte in **W o kW**: la dashboard le normalizza automaticamente in kW.
- `sensor.solar_grid_power`: **positivo = prelievo/import**, **negativo = immissione/export**.
- `sensor.solar_battery_power`: **positivo = carica**, **negativo = scarica**.
- SOC in percentuale; energie giornaliere preferibilmente in kWh.

## Garage, EV e wallbox

- `binary_sensor.ev_charging_at_home`
- `binary_sensor.garage_dehumidifier_tank_full`
- `fan.garage_air_purifier`
- `humidifier.garage_dehumidifier`
- `lock.garage_dehumidifier_child_lock`
- `sensor.garage_air_quality`
- `sensor.garage_dehumidifier_humidity`
- `sensor.garage_dehumidifier_tank_status`
- `sensor.garage_dehumidifier_water_full_time`
- `sensor.garage_dehumidifier_water_level`
- `sensor.garage_humidity`
- `sensor.garage_pm2_5`
- `sensor.garage_temperature`
- `sensor.grid_current_l1`
- `sensor.wallbox_board_temperature`
- `sensor.wallbox_case_temperature`
- `sensor.wallbox_charging_current_l1`
- `sensor.wallbox_charging_power`
- `sensor.wallbox_evse_status`
- `sensor.wallbox_fan_status`
- `sensor.wallbox_max_charging_current`
- `sensor.wallbox_session_energy`
- `sensor.wallbox_status`
- `sensor.wallbox_voltage_l1`
- `switch.garage_air_purifier_power`
- `switch.garage_dehumidifier_buzzer`
- `switch.garage_dehumidifier_display`
- `switch.garage_dehumidifier_power`
- `switch.garage_treadmill`
- `switch.garage_tv`

### Wallbox v1.1.0

La dashboard mostra la potenza di ricarica in kW e mantiene A/V come dettaglio. Per `sensor.wallbox_charging_power` sono supportati sia sensori in W sia in kW. `sensor.grid_current_l1` viene combinato con `sensor.wallbox_voltage_l1` per stimare il carico istantaneo del contatore.

## Robot aspirapolvere

- `image.robot_vacuum_map`
- `number.robot_vacuum_water_flow`
- `select.robot_vacuum_auto_empty_frequency`
- `sensor.robot_vacuum_battery`
- `sensor.robot_vacuum_cleaned_area`
- `sensor.robot_vacuum_cleaning_duration`
- `vacuum.robot_vacuum`

## Riscaldamento e ACS

- `calendar.heating_program`
- `climate.home_heating`
- `sensor.heating_current_temperature`
- `sensor.heating_humidity`
- `sensor.heating_state`
- `sensor.heating_target_temperature`
- `water_heater.domestic_hot_water`

## Altro

- `input_boolean.shower_mode`
- `sensor.entry_illuminance`
- `sensor.utility_room_humidity`
- `sensor.utility_room_temperature`
