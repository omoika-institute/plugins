import omoika
from omoika.elements import TextInput


class HTTPHeaders(omoika.Plugin):
    version = "1.0.0"
    label = "HTTP Headers"
    category = "Web"
    color = "#8B5CF699"
    icon = "brackets"
    author = "omoika"
    description = "Represent HTTP response headers for a URL."

    elements = [
        TextInput(label="URL", icon="link"),
    ]

