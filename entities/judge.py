import omoika
from omoika.elements import TextInput


class Judge(omoika.Plugin):
    version = "1.0.0"
    label = "Judge"
    category = "Identity"
    color = "#60A5FA99"
    icon = "gavel"
    author = "omoika"
    description = "Represent a judge."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Court", icon="building"),
    ]

