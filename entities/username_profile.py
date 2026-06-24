from omoika.elements import TextInput
from omoika import Plugin


class UsernameProfile(Plugin):
    version = "1.0.0"
    label = "Username Profile"
    category = ["Social Media", "Identity"]
    is_available = False
    color = "#8d0a6199"
    icon = "user-scan"
    author = "omoika"
    
    elements = [
        TextInput(label='Profile Link', icon='link'),
    ]
