```
# TEMPLATE SENSORS
- platform: template
  sensors:
    # Tide
    tide_today_1:
      entity_id: sensor.tide_xx_xx_2
      friendly_name_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[0].flag == 'low' %}
          Lavvann
        {% else %}
          Høyvann
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[0].flag == 'low' %}
          mdi:transfer-down
        {% else %}
          mdi:transfer-up
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_xx_xx_2.attributes.water_levels[0].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_xx_xx_2.attributes.water_levels[0].time) | timestamp_custom('%d.%m.%Y %H:%M') }}"

    tide_today_2:
      entity_id: sensor.tide_xx_xx_2
      friendly_name_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[1].flag == 'low' %}
          Lavvann
        {% else %}
          Høyvann
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[1].flag == 'low' %}
          mdi:transfer-down
        {% else %}
          mdi:transfer-up
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_xx_xx_2.attributes.water_levels[1].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_xx_xx_2.attributes.water_levels[1].time) | timestamp_custom('%d.%m.%Y %H:%M') }}"

    tide_today_3:
      entity_id: sensor.tide_xx_xx_2
      friendly_name_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[2].flag == 'low' %}
          Lavvann
        {% else %}
          Høyvann
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[2].flag == 'low' %}
          mdi:transfer-down
        {% else %}
          mdi:transfer-up
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_xx_xx_2.attributes.water_levels[2].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_xx_xx_2.attributes.water_levels[2].time) | timestamp_custom('%d.%m.%Y %H:%M') }}"

    tide_today_4:
      entity_id: sensor.tide_xx_xx_2
      friendly_name_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[3].flag == 'low' %}
          Lavvann
        {% else %}
          Høyvann
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[3].flag == 'low' %}
          mdi:transfer-down
        {% else %}
          mdi:transfer-up
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_xx_xx_2.attributes.water_levels[3].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_xx_xx_2.attributes.water_levels[3].time) | timestamp_custom('%d.%m.%Y %H:%M') }}"

    tide_tomorrow_1:
      entity_id: sensor.tide_xx_xx_2
      friendly_name_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[4].flag == 'low' %}
          Lavvann
        {% else %}
          Høyvann
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[4].flag == 'low' %}
          mdi:transfer-down
        {% else %}
          mdi:transfer-up
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_xx_xx_2.attributes.water_levels[4].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_xx_xx_2.attributes.water_levels[4].time) | timestamp_custom('%d.%m.%Y %H:%M') }}"

    tide_tomorrow_2:
      entity_id: sensor.tide_xx_xx_2
      friendly_name_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[5].flag == 'low' %}
          Lavvann
        {% else %}
          Høyvann
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[5].flag == 'low' %}
          mdi:transfer-down
        {% else %}
          mdi:transfer-up
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_xx_xx_2.attributes.water_levels[5].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_xx_xx_2.attributes.water_levels[5].time) | timestamp_custom('%d.%m.%Y %H:%M') }}"

    tide_tomorrow_3:
      entity_id: sensor.tide_xx_xx_2
      friendly_name_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[6].flag == 'low' %}
          Lavvann
        {% else %}
          Høyvann
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[6].flag == 'low' %}
          mdi:transfer-down
        {% else %}
          mdi:transfer-up
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_xx_xx_2.attributes.water_levels[6].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_xx_xx_2.attributes.water_levels[6].time) | timestamp_custom('%d.%m.%Y %H:%M') }}"

    tide_tomorrow_4:
      entity_id: sensor.tide_xx_xx_2
      friendly_name_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[7].flag == 'low' %}
          Lavvann
        {% else %}
          Høyvann
        {% endif %}
      icon_template: >-
        {% if states.sensor.tide_xx_xx_2.attributes.water_levels[7].flag == 'low' %}
          mdi:transfer-down
        {% else %}
          mdi:transfer-up
        {% endif %}
      unit_of_measurement: "cm"
      value_template: "{{ states.sensor.tide_xx_xx_2.attributes.water_levels[7].value | round(0) }}"
      attribute_templates:
        tidspunkt: "{{ as_timestamp(states.sensor.tide_xx_xx_2.attributes.water_levels[7].time) | timestamp_custom('%d.%m.%Y %H:%M') }}"
```