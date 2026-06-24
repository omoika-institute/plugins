import omoika
from omoika.elements import TextInput


class CryptoTransaction(omoika.Plugin):
    version = "1.0.0"
    label = "Crypto Transaction"
    category = ["Cryptocurrency", "Finance"]
    color = "#F59E0B99"
    icon = "currency"
    author = "omoika"
    description = "Represent a blockchain transaction (hash/network)."

    elements = [
        TextInput(label="Tx Hash", icon="hash"),
        TextInput(label="Network", icon="network"),
    ]
