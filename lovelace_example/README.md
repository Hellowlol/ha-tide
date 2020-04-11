#### How to make a nice Lovelace card of the tide sensor and attributes

In this example we're using HACS plugins "button-card", "card-mod", "Multiple Entity Row" and "Stack in card". You also need a photo for the backgroud. Just find something you like. Aspect ratio 4:3 works well.
This is what my final result looks like:

![Simple](/lovelace_example/ha-tide.PNG)

As you already may have noticed, the language used in the example is norwegian. Tide works only using norwegian coordinates as data is provided by Kartverket.

First thing to do is making some template sensors from some of the attributes.
In sensors.yaml you add:

````
# TEMPLATE SENSORS
- platform: template
  sensors:
    # Tide
    tidevann_tilstand:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name: 'Tidevann'
      icon_template: "{% if is_state('sensor.tide_58_0795928_7_8038319', 'Flow') %}mdi:transfer-up{% else %}mdi:transfer-down{% endif %}"
      value_template: "{% if is_state('sensor.tide_58_0795928_7_8038319', 'Flow') %}Flo sjø{% else %}Fjære sjø{% endif %}"

    tidevann_1:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[0].flag == 'low' %}
          Fjære
        {% else %}
          Flo
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[0].flag == 'low' %}
          mdi:wave
        {% else %}
          mdi:waves
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[0].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[0].time) | timestamp_custom('%d.%m %H:%M') }}"

    tidevann_2:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[1].flag == 'low' %}
          Fjære
        {% else %}
          Flo
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[1].flag == 'low' %}
          mdi:wave
        {% else %}
          mdi:waves
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[1].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[1].time) | timestamp_custom('%d.%m %H:%M') }}"

    tidevann_3:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[2].flag == 'low' %}
          Fjære
        {% else %}
          Flo
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[2].flag == 'low' %}
          mdi:wave
        {% else %}
          mdi:waves
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[2].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[2].time) | timestamp_custom('%d.%m %H:%M') }}"

    tidevann_4:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[3].flag == 'low' %}
          Fjære
        {% else %}
          Flo
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[3].flag == 'low' %}
          mdi:wave
        {% else %}
          mdi:waves
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[3].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[3].time) | timestamp_custom('%d.%m %H:%M') }}"

    tidevann_5:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[4].flag == 'low' %}
          Fjære
        {% else %}
          Flo
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[4].flag == 'low' %}
          mdi:wave
        {% else %}
          mdi:waves
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[4].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[4].time) | timestamp_custom('%d.%m %H:%M') }}"

    tidevann_6:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[5].flag == 'low' %}
          Fjære
        {% else %}
          Flo
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[5].flag == 'low' %}
          mdi:wave
        {% else %}
          mdi:waves
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[5].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[5].time) | timestamp_custom('%d.%m %H:%M') }}"

    tidevann_7:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[6].flag == 'low' %}
          Fjære
        {% else %}
          Flo
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[6].flag == 'low' %}
          mdi:wave
        {% else %}
          mdi:waves
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[6].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[6].time) | timestamp_custom('%d.%m %H:%M') }}"

    tidevann_8:
      entity_id: sensor.tide_58_0795928_7_8038319
      friendly_name_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[7].flag == 'low' %}
          Fjære
        {% else %}
          Flo
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[7].flag == 'low' %}
          mdi:wave
        {% else %}
          mdi:waves
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[7].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_58_0795928_7_8038319.attributes.water_levels[7].time) | timestamp_custom('%d.%m %H:%M') }}"

````

For a complete list of attributes see `zaptec_home_api_data.txt`.

Here are a couple of configuration examples for a single phase installation.
Add the following to your `sensors.yaml` file to make some sensors from the attributes.

#### TEMPLATE SENSORS (change "zch000000" to your charger's id)
````
- platform: template
  sensors:
    zaptec_home_allocated:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger allocated current"
      icon_template: mdi:waves
      unit_of_measurement: "A"
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'charge_current_set') | round(0) }}"

    zaptec_home_current:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger current"
      icon_template: mdi:current-ac
      unit_of_measurement: "A"
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'current_phase1') | round(0) }}"

    zaptec_home_energy:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger energy"
      icon_template: mdi:counter
      unit_of_measurement: "kWh"
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'total_charge_power_session') | round(0) }}"

    zaptec_home_firmware:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger firmware version"
      icon_template: mdi:label
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'smart_computer_software_application_version') }}"

    zaptec_home_humidity:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger humidity"
      icon_template: mdi:water-percent
      unit_of_measurement: "%"
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'humidity') | round(0) }}"

    zaptec_home_mode:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger mode"
      icon_template: mdi:alpha-z-circle-outline
      value_template: >-
        {% if is_state_attr('sensor.zaptec_zch000000', 'charger_operation_mode', '1') %}
          Disconnected
        {% elif is_state_attr('sensor.zaptec_zch000000', 'charger_operation_mode', '2') %}
          Waiting
        {% elif is_state_attr('sensor.zaptec_zch000000', 'charger_operation_mode', '3') %}
          Charging
        {% elif is_state_attr('sensor.zaptec_zch000000', 'charger_operation_mode', '5') %}
          Finished
        {% else %}
          Unknown
        {% endif %}

    zaptec_home_power:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger power"
      icon_template: mdi:power-plug
      unit_of_measurement: "W"
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'total_charge_power') | round(0) }}"

    zaptec_home_signal:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger signal strength"
      icon_template: >-
        {% if state_attr('sensor.zaptec_zch000000', 'communication_signal_strength') | float >= -67 %}
          mdi:wifi-strength-4
        {% elif state_attr('sensor.zaptec_zch000000', 'communication_signal_strength') | float >= -72 %}
          mdi:wifi-strength-3
        {% elif state_attr('sensor.zaptec_zch000000', 'communication_signal_strength') | float >= -80 %}
          mdi:wifi-strength-2
        {% elif state_attr('sensor.zaptec_zch000000', 'communication_signal_strength') | float >= -90 %}
          mdi:wifi-strength-1
        {% else %}
          mdi:wifi-strength-outline
        {% endif %}
      unit_of_measurement: "dBm"
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'communication_signal_strength') }}"

    zaptec_home_state:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger state"
      icon_template: >-
        {% if is_state_attr('sensor.zaptec_zch000000', 'is_online', '1') %}
          mdi:access-point-network
        {% else %}
          mdi:access-point-network-off
        {% endif %}
      value_template: >-
        {% if is_state_attr('sensor.zaptec_zch000000', 'is_online', '1') %}
          Online
        {% else %}
          Offline
        {% endif %}

    zaptec_home_temperature:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger temperature"
      icon_template: mdi:thermometer
      unit_of_measurement: '°C'
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'temperature_internal5') | round(0) }}"

    zaptec_home_voltage:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger voltage"
      icon_template: mdi:flash
      unit_of_measurement: "V"
      value_template: "{{ state_attr('sensor.zaptec_zch000000', 'voltage_phase1') | round(0) }}"

    zaptec_home_warnings:
      entity_id: sensor.zaptec_zch000000
      friendly_name: "Car charger warnings"
      icon_template: mdi:alert-circle-outline
      value_template: >-
        {% if is_state_attr('sensor.zaptec_zch000000', 'warnings', '0') %}
          No warnings
        {% else %}
          Failure
        {% endif %}
````
    
Then add the following to your lovelace configuration to make a simple card in Home Assistant.
````	
  - title: Car charger entity card
    icon: mdi:ev-station
    background: white
    cards:
      - type: vertical-stack
        cards:
          - type: entities
            title: Car charger
            show_header_toggle: false
            entities:
              - sensor.zaptec_home_mode
              - sensor.zaptec_home_state
              - sensor.zaptec_home_signal
              - sensor.zaptec_home_allocated
              - sensor.zaptec_home_temperature
              - sensor.zaptec_home_humidity
              - sensor.zaptec_home_current
              - sensor.zaptec_home_voltage
              - sensor.zaptec_home_power
              - sensor.zaptec_home_energy
              - sensor.zaptec_home_warnings
              - sensor.zaptec_home_firmware
````

And it will look like this:

![Simple](/lovelace_example/car_charger_simple.PNG)

This is an example of a more sophisticated card using the picture-elements card, the circle-sensor custom card and some other custom elements.
For this configuration the images are located in the /www/images directory.
```
  - title: Car charger picture elements
    icon: mdi:ev-station
    cards:
      - type: vertical-stack
        cards:
          - type: picture-elements
            image: /local/images/zaptec-home.png
            title: Car charger
            elements:
              - type: state-label
                entity: sensor.zaptec_home_state
                style:
                  left: 48.5%
                  top: 10%
                  transform: 'translate(-50%,-50%)'
              - type: state-icon
                entity: sensor.zaptec_home_signal
                style:
                  left: 48.7%
                  top: 13%
                  "--paper-item-icon-color": black
                  transform: 'translate(-50%,-50%)'
              - type: state-label
                entity: sensor.zaptec_home_signal
                style:
                  left: 48.5%
                  top: 16%
                  transform: 'translate(-50%,-50%)'
              - type: custom:circle-sensor-card
                entity: sensor.zaptec_home_temperature
                max: 90
                min: -10
                stroke_width: 15
                stroke_color: '#00aaff'
                gradient: true
                fill: rgba(255,255,255,0.6)
                name: Temp.
                units: '°C'
                color_stops:
                  0: '#00aaff'
                  10: '#aaff00'
                  50: '#ffff00'
                  60: '#ffaa00'
                  90: '#ff0055'
                font_style:
                  font-size: 1em
                  font-color: black
                style:
                  top: 20%
                  left: 28%
                  width: 6em
                  height: 6em
                  transform: translate(-50%,-50%)
              - type: custom:circle-sensor-card
                entity: sensor.zaptec_home_humidity
                max: 100
                min: 0
                stroke_width: 15
                stroke_color: '#00aaff'
                gradient: true
                fill: rgba(255,255,255,0.6)
                name: Humidity
                units: '%'
                color_stops:
                  0: '#ffff00'
                  50: '#aaff00'
                  90: '#00aaff'
                  100: '#aa00ff'
                font_style:
                  font-size: 1em
                  font-color: black
                style:
                  top: 20%
                  left: 72%
                  width: 6em
                  height: 6em
                  transform: translate(-50%,-50%)
              - type: custom:circle-sensor-card
                entity: sensor.zaptec_home_current
                max: 32
                min: 0
                stroke_width: 15
                stroke_color: '#00aaff'
                gradient: true
                fill: rgba(255,255,255,0.6)
                name: Current
                units: 'A'
                color_stops:
                  0: '#ffff00'
                  16: '#aaff00'
                  32: '#ffaa00'
                font_style:
                  font-size: 1em
                  font-color: black
                style:
                  top: 47.5%
                  left: 25%
                  width: 6em
                  height: 6em
                  transform: translate(-50%,-50%)
              - type: custom:circle-sensor-card
                entity: sensor.zaptec_home_voltage
                max: 460
                min: 0
                stroke_width: 15
                stroke_color: '#00aaff'
                gradient: true
                fill: rgba(255,255,255,0.6)
                name: Voltage
                units: 'V'
                color_stops:
                  207: '#ffff00'
                  230: '#aaff00'
                  253: '#ff0055'
                font_style:
                  font-size: 1em
                  font-color: black
                style:
                  top: 47.5%
                  left: 75%
                  width: 6em
                  height: 6em
                  transform: translate(-50%,-50%)
              - type: image
                entity: sensor.zaptec_zch000000
                state_image:
                  unknown: /local/images/zh-1.png
                  disconnected: /local/images/zh-1.png
                  waiting: /local/images/zh-2.png
                  charging: /local/images/zh-3.png
                  charge_done: /local/images/zh-5.png
                style:
                  top: 34.5%
                  left: 50%
                  width: 15%
                  transform: translate(-50%,-50%)
              - type: state-label
                entity: sensor.zaptec_home_mode
                style:
                  top: 45.5%
                  left: 48.5%
                  transform: translate(-50%,-50%)
              - type: custom:state-attribute-element
                entity: sensor.zaptec_zch000000
                attribute: smart_computer_software_application_version
                prefix: "Firmware: "
                style:
                  top: 96%
                  left: 48.5%
                  transform: translate(-50%,-50%)
              - type: custom:circle-sensor-card
                entity: sensor.zaptec_home_power
                max: 7350
                min: 0
                stroke_width: 15
                stroke_color: '#00aaff'
                gradient: true
                fill: rgba(255,255,255,0.6)
                name: Power
                units: 'W'
                color_stops:
                  0: '#00aaff'
                  6440: '#aaff00'
                  6900: '#ffff00'
                  7130: '#ffaa00'
                  7360: '#ff0055'
                font_style:
                  font-size: 1em
                  font-color: black
                style:
                  top: 72%
                  left: 34%
                  width: 6em
                  height: 6em
                  transform: 'translate(-50%,-50%)'
              - type: custom:circle-sensor-card
                entity: sensor.zaptec_home_energy
                max: 35
                min: 0
                stroke_width: 15
                stroke_color: '#00aaff'
                gradient: true
                fill: rgba(255,255,255,0.6)
                name: Energy
                units: 'kWh'
                color_stops:
                  31: '#ffff00'
                  33: '#ffaa00'
                  35: '#ff0055'
                font_style:
                  font-size: 1em
                  font-color: black
                style:
                  top: 72%
                  left: 66%
                  width: 6em
                  height: 6em
                  transform: 'translate(-50%,-50%)'
              - type: state-label
                entity: sensor.zaptec_home_allocated
                style:
                  top: 82.5%
                  left: 49%
                  font-size: 28px
                  color: '#ffffff'
                  transform: 'translate(-50%,-50%)'
````

And it will look like this:

![Advanced](/lovelace_example/car_charger_advanced.PNG)
