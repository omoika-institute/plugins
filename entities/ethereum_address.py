import omoika
from omoika.elements import TextInput


class EthereumAddress(omoika.Plugin):
    version = "1.0.0"
    label = "Ethereum Address"
    category = "Cryptocurrency"
    color = "#6366F199"
    icon = "currency-ethereum"
    author = "omoika"
    description = "Represent an Ethereum address."

    elements = [
        TextInput(label="ETH Address", icon="currency-ethereum"),
    ]

