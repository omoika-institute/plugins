import omoika
from omoika.elements import TextInput


class MeetingBusiness(omoika.Plugin):
    version = "1.0.0"
    label = "Meeting Business"
    category = "Events"
    color = "#A78BFA99"
    icon = "briefcase"
    author = "omoika"
    description = "Represent a business meeting."

    elements = [
        TextInput(label="Subject", icon="briefcase"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Location", icon="map-pin"),
    ]

