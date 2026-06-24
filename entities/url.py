from urllib.parse import urlparse
from omoika.elements import TextInput
from omoika import Plugin



class URL(Plugin):
    version = "1.0.0"

    label = 'URL'
    category = "Web"
    author = 'OSIB'
    description = 'Uniform Resource Locator, usually starts with https://'

    color = '#47139699'
    elements = [
        TextInput(label="URL", icon="link"),
    ]
