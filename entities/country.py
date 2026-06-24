import omoika
from omoika.elements import TextInput


class Country(omoika.Plugin):
    version = "1.0.0"
    label = "Country"
    category = "Locations"
    color = "#F59E0B99"
    icon = "flag"
    author = "omoika"
    description = "Represent a country."

    elements = [
        TextInput(label="Name", icon="flag"),
        TextInput(label="ISO Code", icon="hash"),
        TextInput(label="Region", icon="map"),
    ]

