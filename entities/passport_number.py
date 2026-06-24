import omoika
from omoika.elements import TextInput


class PassportNumber(omoika.Plugin):
    version = "1.0.0"
    label = "Passport Number"
    category = "Identity"
    color = "#94A3B899"
    icon = "id"
    author = "omoika"
    description = "Represent a passport number."

    elements = [
        TextInput(label="Number", icon="hash"),
        TextInput(label="Country", icon="flag"),
        TextInput(label="Name", icon="user"),
    ]

