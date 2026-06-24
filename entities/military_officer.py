import omoika
from omoika.elements import TextInput


class MilitaryOfficer(omoika.Plugin):
    version = "1.0.0"
    label = "Military Officer"
    category = "Identity"
    color = "#60A5FA99"
    icon = "military-rank"
    author = "omoika"
    description = "Represent a military officer."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Branch", icon="flag"),
        TextInput(label="Rank", icon="military-rank"),
    ]

