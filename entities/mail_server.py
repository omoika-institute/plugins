import omoika
from omoika.elements import TextInput


class MailServer(omoika.Plugin):
    version = "1.0.0"
    label = "Mail Server"
    category = "Network"
    color = "#DB277799"
    icon = "mail"
    author = "omoika"
    description = "Represent an email (MX) server."

    elements = [
        TextInput(label="MX Host", icon="mail"),
        TextInput(label="Priority", icon="sort-ascending"),
    ]

