import omoika
from omoika.elements import TextInput


class Airport(omoika.Plugin):
    version = "1.0.0"
    label = "Airport"
    category = ["Locations", "Transportation"]
    color = "#3B82F699"
    icon = "plane"
    author = "omoika"
    description = "Represent an airport (IATA/ICAO codes and name)."

    elements = [
        TextInput(label="IATA", icon="letter-a"),
        TextInput(label="ICAO", icon="letter-i"),
        TextInput(label="Name", icon="map"),
        TextInput(label="Country", icon="flag"),
    ]
