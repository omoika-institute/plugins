import omoika
from omoika.elements import TextInput


class Missile(omoika.Plugin):
    version = "1.0.0"
    label = "Missile"
    category = "Weapons"
    color = "#F9731699"
    icon = "rocket"
    author = "omoika"
    description = "Represent a missile system."

    elements = [
        TextInput(label="Designation", icon="tag"),
        TextInput(label="Range", icon="ruler"),
        TextInput(label="Manufacturer", icon="building"),
    ]

