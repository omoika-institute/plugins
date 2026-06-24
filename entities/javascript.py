import omoika
from omoika.elements import TextInput


class JavaScript(omoika.Plugin):
    version = "1.0.0"
    label = "JavaScript"
    category = "Web"
    color = "#EAB30899"
    icon = "brand-javascript"
    author = "omoika"
    description = "Represent a JavaScript resource reference."

    elements = [
        TextInput(label="URL", icon="link"),
        TextInput(label="Hash", icon="hash"),
    ]
