import omoika
from omoika.elements import TextInput


class EmailAddress(omoika.Plugin):
    version = "1.0.0"
    label = "Email Address"
    category = ["Identity", "Communications"]
    color = "#0D948899"
    icon = "at"
    author = "omoika"
    description = "Represent and store an email address."

    elements = [
        TextInput(label="Email", icon="at"),
    ]

