import omoika
from omoika.elements import TextInput


class Gun(omoika.Plugin):
    version = "1.0.0"
    label = "Gun"
    category = "Weapons"
    color = "#9CA3AF99"
    icon = "target"
    author = "omoika"
    description = "Represent a firearm (make/model/serial)."

    elements = [
        TextInput(label="Make", icon="tool"),
        TextInput(label="Model", icon="tools"),
        TextInput(label="Serial Number", icon="hash"),
    ]

