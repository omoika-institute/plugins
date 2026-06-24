import omoika
from omoika.elements import TextInput


class NFTAsset(omoika.Plugin):
    version = "1.0.0"
    label = "NFT Asset"
    category = "Cryptocurrency"
    color = "#A855F799"
    icon = "photo-up"
    author = "omoika"
    description = "Represent an NFT (contract/token ID)."

    elements = [
        TextInput(label="Contract", icon="hash"),
        TextInput(label="Token ID", icon="hash"),
        TextInput(label="Chain", icon="network"),
    ]
