import omoika
from omoika.elements import TextInput


class AutonomousSystem(omoika.Plugin):
    version = "1.0.0"
    label = "Autonomous System"
    category = "Network"
    color = "#06B6D499"
    icon = "router"
    author = "omoika"
    description = "Represent an Autonomous System (ASN)."

    elements = [
        TextInput(label="ASN", icon="router"),
        TextInput(label="Org", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

