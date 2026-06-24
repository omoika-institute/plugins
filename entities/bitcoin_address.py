import omoika
from omoika.elements import TextInput


class BitcoinAddress(omoika.Plugin):
    version = "1.0.0"
    label = "Bitcoin Address"
    category = "Cryptocurrency"
    color = "#F59E0B99"
    icon = "currency-bitcoin"
    author = "omoika"
    description = "Represent a Bitcoin address."

    elements = [
        TextInput(label="BTC Address", icon="currency-bitcoin"),
    ]

