from omoika.elements import Title, Empty, TextInput
import omoika


class IPGeolocation(omoika.Plugin):
    version = "1.0.0"
    label = "IP Geolocation"
    category = ["Network", "Locations"]
    is_available = False
    icon = "map-pin"
    author = "omoika"
    color = "#03A79199"
    elements = [
        [
            TextInput(label="City", icon="map-pin"),
            TextInput(label="State", icon="map-pin"),
        ],
        [
            TextInput(label="Country", icon="map-pin"),
            TextInput(label="Range", icon="access-point"),
        ],
        [
            TextInput(label="Postal", icon="map-pin"),
            TextInput(label="Company", icon="trademark"),
        ],
        [
            TextInput(label="Timezone", icon="clock"),
            TextInput(label="Hosted domains", icon="access-point"),
        ],
        [
            TextInput(label="Coordinates", icon="map-pin"),
            TextInput(label="Privacy", icon="network"),
        ],
        [
            TextInput(label="Abuse Contact", icon="map-pin"),
            TextInput(label="Anycast", icon="network"),
        ],
        [
            Empty(),
            TextInput(label="ASN type", icon="access-point"),
        ],
    ]
