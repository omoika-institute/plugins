import omoika
from omoika.elements import TextInput


class MoneroAddress(omoika.Plugin):
    version = "1.0.0"
    label = "Monero Address"
    category = "Cryptocurrency"
    color = "#FB923C99"
    icon = "currency"
    author = "omoika"
    description = "Represent a Monero (XMR) address."

    elements = [
        TextInput(label="XMR Address", icon="currency"),
    ]

