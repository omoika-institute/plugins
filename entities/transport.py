import omoika
from omoika.elements import TextInput


class Transport(omoika.Plugin):
    version = "1.0.0"
    label = "Transport"
    category = "Transportation"
    color = "#94A3B899"
    icon = "road"
    author = "omoika"
    description = "Represent a transport item or reference."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Identifier", icon="hash"),
    ]

