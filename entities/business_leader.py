import omoika
from omoika.elements import TextInput


class BusinessLeader(omoika.Plugin):
    version = "1.0.0"
    label = "Business Leader"
    category = ["Identity", "Organizations"]
    color = "#F59E0B99"
    icon = "briefcase"
    author = "omoika"
    description = "Represent an executive or business leader."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Company", icon="building"),
        TextInput(label="Title", icon="id"),
    ]

