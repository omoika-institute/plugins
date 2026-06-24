import omoika
from omoika.elements import TextInput


class ConversationEmail(omoika.Plugin):
    version = "1.0.0"
    label = "Conversation Email"
    category = "Communications"
    color = "#A78BFA99"
    icon = "mail"
    author = "omoika"
    description = "Represent an email thread or subject."

    elements = [
        TextInput(label="Subject", icon="mail"),
        TextInput(label="From", icon="at"),
        TextInput(label="To", icon="at"),
    ]

