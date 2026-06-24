from omoika.elements import CopyText, TextAreaInput, Empty
import omoika


class Whois(omoika.Plugin):
    version = "1.0.0"
    label = "Whois"
    category = "Web"
    is_available = False
    color = "#F47C0099"
    elements = [
        TextAreaInput(label="Raw WHOIS"),
        [Empty(), Empty()]
    ]
    icon = "world-question"
    author = "omoika"
    description = "whois.com allows you to trace the ownership and tenure of a domain name or an IP address"
