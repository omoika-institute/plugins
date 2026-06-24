import omoika
from omoika.elements import TextInput


class TransportHub(omoika.Plugin):
    version = "1.0.0"
    label = "Transport Hub"
    category = ["Locations", "Transportation"]
    color = "#9CA3AF99"
    icon = "building-stadium"
    author = "omoika"
    description = "Represent a transport hub (airport/station/port)."

    elements = [
        TextInput(label="Name", icon="building"),
        TextInput(label="Type", icon="tag"),
        TextInput(label="City", icon="building"),
    ]

