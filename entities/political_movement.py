import omoika
from omoika.elements import TextInput


class PoliticalMovement(omoika.Plugin):
    version = "1.0.0"
    label = "Political Movement"
    category = "Organizations"
    color = "#60A5FA99"
    icon = "flag"
    author = "omoika"
    description = "Represent a political movement."

    elements = [
        TextInput(label="Name", icon="flag"),
        TextInput(label="Country", icon="flag"),
        TextInput(label="Ideology", icon="tag"),
    ]

