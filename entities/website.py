import socket
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from omoika.elements import TextInput
from omoika.errors import PluginError
import omoika


class Website(omoika.Plugin):
    version = "1.0.0"

    label = "Website"
    category = "Web"
    description = "Represents a domain from a website on the internet"
    author = "omoika"
    
    color = "#1D1DB899"
    icon = "world-www"
    
    elements = [
        TextInput(label="Domain", icon="world-www"),
    ]


