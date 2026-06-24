import omoika
from omoika.elements import TextInput


class Weapon(omoika.Plugin):
    version = "1.0.0"
    label = "Weapon"
    category = "Weapons"
    color = "#9CA3AF99"
    icon = "target"
    author = "omoika"
    description = "Represent a weapon (generic)."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Make/Model", icon="tools"),
        TextInput(label="Serial", icon="hash"),
    ]

