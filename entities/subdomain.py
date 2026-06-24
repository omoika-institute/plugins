from omoika.elements import TextInput
import omoika


class Subdomain(omoika.Plugin):
    version = "1.0.0"
    label = "Subdomain"
    category = "Web"
    is_available = True
    description = "A domain that is a part of another domain"
    color = "#093FB499"
    elements = [
        TextInput(label="Subdomain", icon="world"),
    ]
    icon = "submarine"
    author = 'OSIB'
