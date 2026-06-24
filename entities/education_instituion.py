import omoika
from omoika.elements import TextInput


class EducationInstituion(omoika.Plugin):
    version = "1.0.0"
    label = "Education Instituion"
    category = "Organizations"
    color = "#A78BFA99"
    icon = "school"
    author = "omoika"
    description = "Represent an educational institution."

    elements = [
        TextInput(label="Name", icon="school"),
        TextInput(label="City", icon="building"),
        TextInput(label="Country", icon="flag"),
    ]

