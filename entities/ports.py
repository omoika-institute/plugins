import omoika
from omoika.elements import TextInput


class Ports(omoika.Plugin):
    version = "1.0.0"
    label = "Ports"
    category = ["Locations", "Transportation"]
    color = "#0EA5E999"
    icon = "plug"
    author = "omoika"
    description = "Represent a service port and protocol."

    elements = [
        TextInput(label="Port", icon="hash"),
        TextInput(label="Protocol", icon="plug"),
        TextInput(label="Service", icon="server"),
    ]
