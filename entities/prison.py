import omoika
from omoika.elements import TextInput


class Prison(omoika.Plugin):
    version = "1.0.0"
    label = "Prison"
    category = "Locations"
    color = "#94A3B899"
    icon = "building-arch"
    author = "omoika"
    description = "Represent a prison or detention facility."

    elements = [
        TextInput(label="Name", icon="building-arch"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

