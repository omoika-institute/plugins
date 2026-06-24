import omoika
from omoika.elements import TextInput


class MacAddress(omoika.Plugin):
    version = "1.0.0"
    label = "MAC Address"
    category = "Network"
    color = "#94A3B899"
    icon = "cpu"
    author = "omoika"
    description = "Represent a device MAC address."

    elements = [
        TextInput(label="MAC", icon="hash"),
        TextInput(label="Vendor", icon="building"),
    ]

