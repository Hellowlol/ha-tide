### How to make a nice Lovelace card using Tide sensor and it's attributes

In this example we're using HACS plugins "button-card", "card-mod", "Multiple Entity Row" and "Stack in card". You also need a photo for the backgroud. Just find something you like. Aspect ratio 4:3 works well.
This is what my final result looks like:

![Simple](/lovelace_example/ha-tide.PNG)

As you may have noticed, the language used in the example is norwegian. Tide only works using norwegian coordinates as data is provided by Kartverket.

First thing to do is to make template sensors from some of the attributes. Your sensor's entity id is presumably something other than mine. Remember to replace "sensor.tide_58_0795928_7_8038319" with your own.
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
Now, the lovelace card is ready made.
