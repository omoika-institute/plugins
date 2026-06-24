import omoika
from omoika.elements import TextInput


class BusinessMan(omoika.Plugin):
    version = "1.0.0"
    label = "Business Man"
    category = ["Identity", "Organizations"]
    color = "#22C55E99"
    icon = "tie"
    author = "omoika"
    description = "Represent a businessman or professional."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Company", icon="building"),
        TextInput(label="Role", icon="id"),
    ]

