import omoika
from omoika.elements import TextInput


class Meeting(omoika.Plugin):
    version = "1.0.0"
    label = "Meeting"
    category = "Events"
    color = "#22C55E99"
    icon = "calendar"
    author = "omoika"
    description = "Represent a generic meeting."

    elements = [
        TextInput(label="Topic", icon="calendar"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

