import omoika
from omoika.elements import TextInput


class Gang(omoika.Plugin):
    version = "1.0.0"
    label = "Gang"
    category = "Organizations"
    color = "#F43F5E99"
    icon = "users-group"
    author = "omoika"
    description = "Represent a gang or criminal group."

    elements = [
        TextInput(label="Name", icon="users-group"),
        TextInput(label="Territory", icon="map"),
    ]

