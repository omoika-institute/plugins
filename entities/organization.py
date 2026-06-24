import omoika
from omoika.elements import TextInput


class Organization(omoika.Plugin):
    version = "1.0.0"
    label = "Organization"
    category = "Organizations"
    color = "#F59E0B99"
    icon = "building"
    author = "omoika"
    description = "Represent an organization entity."

    elements = [
        TextInput(label="Name", icon="building"),
        TextInput(label="Type", icon="tag"),
        TextInput(label="Country", icon="flag"),
    ]

