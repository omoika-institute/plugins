import omoika
from omoika.elements import TextInput


class Shop(omoika.Plugin):
    version = "1.0.0"
    label = "Shop"
    category = "Organizations"
    color = "#FDE04799"
    icon = "building-store"
    author = "omoika"
    description = "Represent a shop or retail location."

    elements = [
        TextInput(label="Name", icon="building-store"),
        TextInput(label="Address", icon="home"),
        TextInput(label="City", icon="building"),
    ]

