import omoika
from omoika.elements import TextInput


class City(omoika.Plugin):
    version = "1.0.0"
    label = "City"
    category = "Locations"
    color = "#60A5FA99"
    icon = "building"
    author = "omoika"
    description = "Represent a city."

    elements = [
        TextInput(label="Name", icon="building"),
        TextInput(label="Country", icon="flag"),
        TextInput(label="Region", icon="map"),
    ]

