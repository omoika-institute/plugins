import omoika
from omoika.elements import TextInput


class Male(omoika.Plugin):
    version = "1.0.0"
    label = "Male"
    category = "Identity"
    color = "#60A5FA99"
    icon = "gender-male"
    author = "omoika"
    description = "Represent a male person."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Age", icon="calendar"),
    ]

