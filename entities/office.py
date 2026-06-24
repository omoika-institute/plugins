import omoika
from omoika.elements import TextInput


class Office(omoika.Plugin):
    version = "1.0.0"
    label = "Office"
    category = "Locations"
    color = "#FDE04799"
    icon = "building"
    author = "omoika"
    description = "Represent an office location."

    elements = [
        TextInput(label="Address", icon="home"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

