import omoika
from omoika.elements import TextInput


class CertificateTransparency(omoika.Plugin):
    version = "1.0.0"
    label = "Certificate Transparency"
    category = "Web"
    color = "#14B8A699"
    icon = "shield-check"
    author = "omoika"
    description = "Represent a CT log entry or lookup."

    elements = [
        TextInput(label="Domain", icon="world-www"),
        TextInput(label="Log ID", icon="shield-check"),
    ]

