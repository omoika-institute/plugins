import omoika
from omoika.elements import TextInput


class SSLCertificate(omoika.Plugin):
    version = "1.0.0"
    label = "SSL Certificate"
    category = "Web"
    color = "#0EA5E999"
    icon = "certificate-2"
    author = "omoika"
    description = "Represent details from an SSL/TLS certificate."

    elements = [
        TextInput(label="Common Name", icon="certificate-2"),
        TextInput(label="Issuer", icon="shield"),
        TextInput(label="Fingerprint", icon="fingerprint"),
    ]

