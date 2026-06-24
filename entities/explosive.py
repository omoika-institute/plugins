import omoika
from omoika.elements import TextInput


class Explosive(omoika.Plugin):
    version = "1.0.0"
    label = "Explosive"
    category = "Weapons"
    color = "#F9731699"
    icon = "flame"
    author = "omoika"
    description = "Represent an explosive material or device."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Weight", icon="scale"),
    ]

