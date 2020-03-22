## Tide a (norwegian tide water) sensor for HASS.


## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `tide`.
4. Download _all_ the files from the `custom_components/tide/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. Choose:
   - Add `tide:` to your HA configuration.
   - In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "tide"

Using your HA configuration directory (folder) as a starting point you should now also have this:


## Configuration options
Key | Type | Required | Default | Description
-- | -- | -- | -- | --
`lat` | `string` | `True` | `""` | Latitude
`lon` | `string` | `True` | `""` | Longitude


## Example sensors.yaml
````yaml
- platform: tide
  longitude: 7.000001
  latitude: 58.0791111
````
