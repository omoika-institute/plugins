import omoika
from omoika.elements import TextInput


class Computer(omoika.Plugin):
    version = "1.0.0"
    label = "Computer"
    category = "Devices"
    color = "#22D3EE99"
    icon = "device-desktop"
    author = "omoika"
    description = "Represent a computer asset."

    elements = [
        TextInput(label="Hostname", icon="device-desktop"),
        TextInput(label="IP Address", icon="map-pin"),
        TextInput(label="OS", icon="cpu"),
    ]

