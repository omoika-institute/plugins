import omoika
from omoika.elements import TextInput


class Region(omoika.Plugin):
    version = "1.0.0"
    label = "Region"
    category = "Locations"
    color = "#60A5FA99"
    icon = "map"
    author = "omoika"
    description = "Represent a geographic region."

    elements = [
        TextInput(label="Name", icon="map"),
        TextInput(label="Country", icon="flag"),
    ]

