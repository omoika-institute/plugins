import omoika
from omoika.elements import TextInput


class PhoneNumber(omoika.Plugin):
    version = "1.0.0"
    label = "Phone Number"
    category = ["Identity", "Communications"]
    color = "#10B98199"
    icon = "phone"
    author = "omoika"
    description = "Represent and store a phone number (E.164)."

    elements = [
        TextInput(label="Phone", icon="phone"),
    ]

