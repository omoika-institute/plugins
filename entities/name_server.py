import omoika
from omoika.elements import TextInput


class NameServer(omoika.Plugin):
    version = "1.0.0"
    label = "Name Server"
    category = "Network"
    color = "#EF444499"
    icon = "server"
    author = "omoika"
    description = "Represent a DNS nameserver (NS)."

    elements = [
        TextInput(label="NS Host", icon="server"),
        TextInput(label="IP Address", icon="map-pin"),
    ]

