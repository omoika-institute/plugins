import omoika
from omoika.elements import TextInput


class RobotsTxt(omoika.Plugin):
    version = "1.0.0"
    label = "robots.txt"
    category = "Web"
    color = "#9CA3AF99"
    icon = "file-text"
    author = "omoika"
    description = "Represent a robots.txt reference for a domain."

    elements = [
        TextInput(label="Domain", icon="world-www"),
        TextInput(label="URL", icon="link"),
    ]
