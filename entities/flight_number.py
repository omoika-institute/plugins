import omoika
from omoika.elements import TextInput


class FlightNumber(omoika.Plugin):
    version = "1.0.0"
    label = "Flight Number"
    category = "Transportation"
    color = "#38BDF899"
    icon = "plane"
    author = "omoika"
    description = "Represent an airline flight number."

    elements = [
        TextInput(label="Airline", icon="plane"),
        TextInput(label="Flight", icon="hash"),
        TextInput(label="Date", icon="calendar"),
    ]

