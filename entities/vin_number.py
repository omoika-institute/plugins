import omoika
from omoika.elements import TextInput


class VinNumber(omoika.Plugin):
    version = "1.0.0"
    label = "VIN Number"
    category = "Transportation"
    color = "#9CA3AF99"
    icon = "hash"
    author = "omoika"
    description = "Represent a Vehicle Identification Number."

    elements = [
        TextInput(label="VIN", icon="hash"),
        TextInput(label="Make", icon="tool"),
        TextInput(label="Model", icon="tools"),
    ]

