import omoika
from omoika.elements import TextInput


class Incident(omoika.Plugin):
    version = "1.0.0"
    label = "Incident"
    category = "Events"
    color = "#F59E0B99"
    icon = "alert-triangle"
    author = "omoika"
    description = "Represent a security or criminal incident."

    elements = [
        TextInput(label="Case ID", icon="hash"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

