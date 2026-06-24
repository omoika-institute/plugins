import omoika
from omoika.elements import TextInput


class MeetingSocial(omoika.Plugin):
    version = "1.0.0"
    label = "Meeting Social"
    category = "Events"
    color = "#FB718599"
    icon = "users"
    author = "omoika"
    description = "Represent a social meeting or gathering."

    elements = [
        TextInput(label="Occasion", icon="users"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

