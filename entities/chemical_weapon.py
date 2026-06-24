import omoika
from omoika.elements import TextInput


class ChemicalWeapon(omoika.Plugin):
    version = "1.0.0"
    label = "Chemical Weapon"
    category = "Weapons"
    color = "#F43F5E99"
    icon = "flask"
    author = "omoika"
    description = "Represent a chemical weapon classification."

    elements = [
        TextInput(label="Agent", icon="flask"),
        TextInput(label="Designation", icon="tag"),
    ]

