import omoika
from omoika.elements import TextInput


class LawOfficer(omoika.Plugin):
    version = "1.0.0"
    label = "Law Officer"
    category = "Identity"
    color = "#22C55E99"
    icon = "badge"
    author = "omoika"
    description = "Represent a law enforcement officer."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Agency", icon="building"),
        TextInput(label="Badge Number", icon="id"),
    ]

