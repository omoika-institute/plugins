import omoika
from omoika.elements import TextInput


class GangLeader(omoika.Plugin):
    version = "1.0.0"
    label = "Gang Leader"
    category = "Identity"
    color = "#EF444499"
    icon = "user-star"
    author = "omoika"
    description = "Represent a gang leader."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Gang", icon="users-group"),
        TextInput(label="Alias", icon="mask"),
    ]

