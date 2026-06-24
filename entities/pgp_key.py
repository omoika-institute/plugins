import omoika
from omoika.elements import TextInput


class PGPKey(omoika.Plugin):
    version = "1.0.0"
    label = "PGP Key"
    category = "Documents"
    color = "#22C55E99"
    icon = "key"
    author = "omoika"
    description = "Represent a PGP public key reference."

    elements = [
        TextInput(label="Key ID", icon="key"),
        TextInput(label="Fingerprint", icon="fingerprint"),
        TextInput(label="Email", icon="at"),
    ]
