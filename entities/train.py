import omoika
from omoika.elements import TextInput


class Train(omoika.Plugin):
    version = "1.0.0"
    label = "Train"
    category = "Transportation"
    color = "#A78BFA99"
    icon = "train"
    author = "omoika"
    description = "Represent a train identifier."

    elements = [
        TextInput(label="Operator", icon="building"),
        TextInput(label="Number", icon="hash"),
        TextInput(label="Route", icon="road"),
    ]

