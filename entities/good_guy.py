import omoika
from omoika.elements import TextInput


class GoodGuy(omoika.Plugin):
    version = "1.0.0"
    label = "Good Guy"
    category = "Identity"
    color = "#22C55E99"
    icon = "user-plus"
    author = "omoika"
    description = "Represent an ally or friendly individual."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Affiliation", icon="users"),
        TextInput(label="Role", icon="id"),
    ]

