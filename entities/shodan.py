import omoika
from omoika.elements import TextInput


class Shodan(omoika.Plugin):
    version = "1.0.0"
    label = "Shodan"
    category = "Search"
    color = "#22C55E99"
    icon = "database-search"
    author = "omoika"
    description = "Represent a Shodan query or result reference."

    elements = [
        TextInput(label="Query", icon="search"),
        TextInput(label="Host IP", icon="map-pin"),
    ]

