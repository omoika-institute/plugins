import omoika
from omoika.elements import TextInput


class GangMember(omoika.Plugin):
    version = "1.0.0"
    label = "Gang Member"
    category = "Identity"
    color = "#FB718599"
    icon = "user"
    author = "omoika"
    description = "Represent a gang member."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Gang", icon="users-group"),
        TextInput(label="Alias", icon="mask"),
    ]

