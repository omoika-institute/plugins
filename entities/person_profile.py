import omoika
from omoika.elements import TextInput


class PersonProfile(omoika.Plugin):
    version = "1.0.0"
    label = "Person Profile"
    category = "Identity"
    color = "#6366F199"
    icon = "user"
    author = "omoika"
    description = "Store basic person profile details."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Username", icon="user-search"),
        TextInput(label="Location", icon="map"),
    ]

