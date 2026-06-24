import omoika
from omoika.elements import TextInput


class OnlineGroup(omoika.Plugin):
    version = "1.0.0"
    label = "Online Group"
    category = ["Social Media", "Organizations"]
    color = "#A78BFA99"
    icon = "users"
    author = "omoika"
    description = "Represent an online group or community."

    elements = [
        TextInput(label="Platform", icon="world-www"),
        TextInput(label="Group Name", icon="users"),
        TextInput(label="URL", icon="link"),
    ]

