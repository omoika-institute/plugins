import omoika
from omoika.elements import TextInput


class FileHash(omoika.Plugin):
    version = "1.0.0"
    label = "File Hash"
    category = ["Documents", "Threat Intelligence"]
    color = "#F9731699"
    icon = "hash"
    author = "omoika"
    description = "Represent a file hash (MD5/SHA1/SHA256)."

    elements = [
        TextInput(label="Hash", icon="hash"),
        TextInput(label="Algorithm", icon="settings"),
    ]

