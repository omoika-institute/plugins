from omoika import Plugin
from omoika.elements import TextInput

class IP(Plugin):
    version = "1.0.0"
    label = "IP"
    category = "Network"
    color = "#E6521F99"
    elements = [TextInput(label="IP Address", icon="map-pin")]
    icon = "building-broadcast-tower"
    author = "omoika"
    description = "Internet Protocol address"
