import omoika
from omoika.elements import TextInput


class MobileComputer(omoika.Plugin):
    version = "1.0.0"
    label = "Mobile Computer"
    category = "Devices"
    color = "#22D3EE99"
    icon = "device-laptop"
    author = "omoika"
    description = "Represent a laptop or tablet."

    elements = [
        TextInput(label="Hostname", icon="device-laptop"),
        TextInput(label="OS", icon="cpu"),
        TextInput(label="Owner", icon="user"),
    ]

