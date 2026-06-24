import omoika
from omoika.elements import TextInput


class IOCIndicator(omoika.Plugin):
    version = "1.0.0"
    label = "IOC Indicator"
    category = "Threat Intelligence"
    color = "#F43F5E99"
    icon = "alert-triangle"
    author = "omoika"
    description = "Represent an Indicator of Compromise (type/value)."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Value", icon="hash"),
    ]
