import omoika
from omoika.elements import TextInput


class Bike(omoika.Plugin):
    version = "1.0.0"
    label = "Bike"
    category = "Transportation"
    color = "#22C55E99"
    icon = "bike"
    author = "omoika"
    description = "Represent a bicycle with make/model."

    elements = [
        TextInput(label="Make", icon="tool"),
        TextInput(label="Model", icon="tools"),
        TextInput(label="Serial Number", icon="hash"),
    ]

