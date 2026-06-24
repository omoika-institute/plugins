import omoika
from omoika.elements import TextInput


class Smartphone(omoika.Plugin):
    version = "1.0.0"
    label = "Smartphone"
    category = "Devices"
    color = "#22C55E99"
    icon = "device-mobile"
    author = "omoika"
    description = "Represent a smartphone device."

    elements = [
        TextInput(label="IMEI", icon="hash"),
        TextInput(label="OS", icon="cpu"),
        TextInput(label="Owner", icon="user"),
    ]

