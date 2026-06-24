import omoika
from omoika.elements import TextInput


class ConversationPhone(omoika.Plugin):
    version = "1.0.0"
    label = "Conversation Phone"
    category = "Communications"
    color = "#06B6D499"
    icon = "phone"
    author = "omoika"
    description = "Represent a phone conversation record."

    elements = [
        TextInput(label="Caller", icon="phone"),
        TextInput(label="Callee", icon="phone"),
        TextInput(label="Time", icon="clock"),
    ]

