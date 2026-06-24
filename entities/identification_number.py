import omoika
from omoika.elements import TextInput


class IdentificationNumber(omoika.Plugin):
    version = "1.0.0"
    label = "Identification Number"
    category = "Identity"
    color = "#94A3B899"
    icon = "id"
    author = "omoika"
    description = "Represent a government-issued ID number."

    elements = [
        TextInput(label="Type", icon="tag"),
        TextInput(label="Number", icon="hash"),
        TextInput(label="Country", icon="flag"),
    ]

