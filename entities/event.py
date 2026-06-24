import omoika
from omoika.elements import TextInput


class Event(omoika.Plugin):
    version = "1.0.0"
    label = "Event"
    category = "Events"
    color = "#60A5FA99"
    icon = "calendar-event"
    author = "omoika"
    description = "Represent an event occurrence."

    elements = [
        TextInput(label="Name", icon="calendar-event"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

