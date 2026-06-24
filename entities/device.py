import omoika
from omoika.elements import TextInput


class Device(omoika.Plugin):
    version = "1.0.0"
    label = "Device"
    category = "Devices"
    color = "#94A3B899"
    icon = "device-mobile"
    author = "omoika"
    description = "Represent a generic device."

    elements = [
        TextInput(label="Identifier", icon="hash"),
        TextInput(label="Type", icon="tag"),
        TextInput(label="Owner", icon="user"),
    ]

