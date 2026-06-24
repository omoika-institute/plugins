import omoika
from omoika.elements import TextInput


class Bus(omoika.Plugin):
    version = "1.0.0"
    label = "Bus"
    category = "Transportation"
    color = "#A78BFA99"
    icon = "bus"
    author = "omoika"
    description = "Represent a bus vehicle identifier."

    elements = [
        TextInput(label="VIN", icon="hash"),
        TextInput(label="Registration", icon="hash"),
        TextInput(label="Route", icon="road"),
    ]

