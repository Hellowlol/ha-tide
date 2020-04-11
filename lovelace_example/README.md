#### How to make a nice Lovelace card of the tide sensor and attributes

In this example we're using HACS plugins "button-card", "card-mod", "Multiple Entity Row" and "Stack in card". You also need a photo for the backgroud. Just find something you like. Aspect ratio 4:3 works well.
This is what my final result looks like:

![Simple](/lovelace_example/ha-tide.PNG)

As you already may have noticed, the language used in the example is norwegian. Tide works only using norwegian coordinates as data is provided by Kartverket.

First thing to do is to make template sensors from some of the attributes.
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

Save and restart HA to see that the template sensors works.

Now it's time to make the lovelace card.
This example is based on using ui-lovelace.yaml (mode: yaml # in configuration.yaml). As you'll see it takes a lot of repeating code to configure the button-card objects. Usually best practice is to make templates to use with the button-card. Templates is outside the the scope of this example, and making templates is very well explained by RomRaider in the button-card repository.

In this example the lovelace card is placed in it's own view called "Flo og fjære". Add the following code to the desired location in your ui-lovelace.yaml file:

````
title: My Home Assistant
views:
  - title: Flo og Fjære
    icon: mdi:wave
    background: white
    cards:
      - type: vertical-stack
        cards:
          - type: custom:stack-in-card
            title: Flo og fjære
            mode: vertical
            keep:
              margin: false
              outer_padding: false
            style: |
              ha-card {
                background: url(/local/images/tidevann.png);
                border-radius: 10px;
                padding-bottom: 5px;
            cards:
              - type: vertical-stack
                cards:
                  - type: entities
                    entities:
                      - sensor.tidevann_tilstand
                      - entity: sensor.tide_58_0795928_7_8038319
                        type: custom:multiple-entity-row
                        name: Målestasjon
                        show_state: false
                        entities:
                          - attribute: delay
                            name: Forsinkelse
                            unit: "min"
                          - attribute: factor
                            name: Faktor
                          - attribute: obsname
                            name: Stasjon
              - type: horizontal-stack
                cards:
                  - type: custom:button-card
                    color_type: blank-card
                    styles:
                      card:
                        - width: 5px
                  - type: custom:button-card
                    entity: sensor.tidevann_1
                    label: >
                      [[[
                        return states['sensor.tidevann_1'].attributes.tidspunkt;
                      ]]]
                    show_state: true
                    show_label: true
                    aspect_ratio: 1/1.5
                    tap_action:
                      action: more_info
                    styles:
                      grid:
                        - grid-template-areas: '"l" "i" "n" "s"'
                        - grid-template-columns: 1fr
                        - grid-template-rows: min-content 1fr min-content min-content
                      img_cell:
                        - align-self: start
                        - text-align: start
                        - margin-right: 10px
                        - margin-left: 0px
                      icon:
                        - width: 35%
                        - margin-left: 5px
                      name:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 16px
                        - font-weight: bold
                        - color: black
                      state:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 14px
                      label:
                        - justify-self: center
                        - padding-top: 10px
                        - font-family: Helvetica
                        - font-size: 12px
                        - color: black
                    state:
                      - operator: "default"
                        styles:
                          card:
                            - background: rgba(252,252,252,.5)
                            - border-radius: 5px
                          icon:
                            - color: '#00a6f8'
                  - type: custom:button-card
                    color_type: blank-card
                    styles:
                      card:
                        - width: 5px
                  - type: custom:button-card
                    entity: sensor.tidevann_2
                    label: >
                      [[[
                        return states['sensor.tidevann_2'].attributes.tidspunkt;
                      ]]]
                    show_state: true
                    show_label: true
                    aspect_ratio: 1/1.5
                    tap_action:
                      action: more_info
                    styles:
                      grid:
                        - grid-template-areas: '"l" "i" "n" "s"'
                        - grid-template-columns: 1fr
                        - grid-template-rows: min-content 1fr min-content min-content
                      img_cell:
                        - align-self: start
                        - text-align: start
                        - margin-right: 10px
                        - margin-left: 0px
                      icon:
                        - width: 35%
                        - margin-left: 5px
                      name:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 16px
                        - font-weight: bold
                        - color: black
                      state:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 14px
                      label:
                        - justify-self: center
                        - padding-top: 10px
                        - font-family: Helvetica
                        - font-size: 12px
                        - color: black
                    state:
                      - operator: "default"
                        styles:
                          card:
                            - background: rgba(252,252,252,.5)
                            - border-radius: 5px
                          icon:
                            - color: '#00a6f8'
                  - type: custom:button-card
                    color_type: blank-card
                    styles:
                      card:
                        - width: 5px
                  - type: custom:button-card
                    entity: sensor.tidevann_3
                    label: >
                      [[[
                        return states['sensor.tidevann_3'].attributes.tidspunkt;
                      ]]]
                    show_state: true
                    show_label: true
                    aspect_ratio: 1/1.5
                    tap_action:
                      action: more_info
                    styles:
                      grid:
                        - grid-template-areas: '"l" "i" "n" "s"'
                        - grid-template-columns: 1fr
                        - grid-template-rows: min-content 1fr min-content min-content
                      img_cell:
                        - align-self: start
                        - text-align: start
                        - margin-right: 10px
                        - margin-left: 0px
                      icon:
                        - width: 35%
                        - margin-left: 5px
                      name:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 16px
                        - font-weight: bold
                        - color: black
                      state:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 14px
                      label:
                        - justify-self: center
                        - padding-top: 10px
                        - font-family: Helvetica
                        - font-size: 12px
                        - color: black
                    state:
                      - operator: "default"
                        styles:
                          card:
                            - background: rgba(252,252,252,.5)
                            - border-radius: 5px
                          icon:
                            - color: '#00a6f8'
                  - type: custom:button-card
                    color_type: blank-card
                    styles:
                      card:
                        - width: 5px
                  - type: custom:button-card
                    entity: sensor.tidevann_4
                    label: >
                      [[[
                        return states['sensor.tidevann_4'].attributes.tidspunkt;
                      ]]]
                    show_state: true
                    show_label: true
                    aspect_ratio: 1/1.5
                    tap_action:
                      action: more_info
                    styles:
                      grid:
                        - grid-template-areas: '"l" "i" "n" "s"'
                        - grid-template-columns: 1fr
                        - grid-template-rows: min-content 1fr min-content min-content
                      img_cell:
                        - align-self: start
                        - text-align: start
                        - margin-right: 10px
                        - margin-left: 0px
                      icon:
                        - width: 35%
                        - margin-left: 5px
                      name:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 16px
                        - font-weight: bold
                        - color: black
                      state:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 14px
                      label:
                        - justify-self: center
                        - padding-top: 10px
                        - font-family: Helvetica
                        - font-size: 12px
                        - color: black
                    state:
                      - operator: "default"
                        styles:
                          card:
                            - background: rgba(252,252,252,.5)
                            - border-radius: 5px
                          icon:
                            - color: '#00a6f8'
                  - type: custom:button-card
                    color_type: blank-card
                    styles:
                      card:
                        - width: 5px
                  - type: custom:button-card
                    entity: sensor.tidevann_5
                    label: >
                      [[[
                        return states['sensor.tidevann_5'].attributes.tidspunkt;
                      ]]]
                    show_state: true
                    show_label: true
                    aspect_ratio: 1/1.5
                    tap_action:
                      action: more_info
                    styles:
                      grid:
                        - grid-template-areas: '"l" "i" "n" "s"'
                        - grid-template-columns: 1fr
                        - grid-template-rows: min-content 1fr min-content min-content
                      img_cell:
                        - align-self: start
                        - text-align: start
                        - margin-right: 10px
                        - margin-left: 0px
                      icon:
                        - width: 35%
                        - margin-left: 5px
                      name:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 16px
                        - font-weight: bold
                        - color: black
                      state:
                        - justify-self: center
                        - font-family: Helvetica
                        - font-size: 14px
                      label:
                        - justify-self: center
                        - padding-top: 10px
                        - font-family: Helvetica
                        - font-size: 12px
                        - color: black
                    state:
                      - operator: "default"
                        styles:
                          card:
                            - background: rgba(252,252,252,.5)
                            - border-radius: 5px
                          icon:
                            - color: '#00a6f8'
                  - type: custom:button-card
                    color_type: blank-card
                    styles:
                      card:
                        - width: 5px

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
