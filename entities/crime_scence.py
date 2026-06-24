import omoika
from omoika.elements import TextInput


class CrimeScence(omoika.Plugin):
    version = "1.0.0"
    label = "Crime Scence"
    category = ["Events", "Locations"]
    color = "#EF444499"
    icon = "alert-triangle"
    author = "omoika"
    description = "Represent a crime scene reference (location/time)."

    elements = [
        TextInput(label="Location", icon="map-pin"),
        TextInput(label="Time", icon="clock"),
        TextInput(label="Case ID", icon="hash"),
    ]

