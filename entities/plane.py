import omoika
from omoika.elements import TextInput


class Plane(omoika.Plugin):
    version = "1.0.0"
    label = "Plane"
    category = "Transportation"
    color = "#38BDF899"
    icon = "plane"
    author = "omoika"
    description = "Represent an aircraft."

    elements = [
        TextInput(label="Tail Number", icon="hash"),
        TextInput(label="Model", icon="tools"),
        TextInput(label="Airline", icon="plane"),
    ]

