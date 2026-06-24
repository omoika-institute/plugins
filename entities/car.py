import omoika
from omoika.elements import TextInput


class Car(omoika.Plugin):
    version = "1.0.0"
    label = "Car"
    category = "Transportation"
    color = "#3B82F699"
    icon = "car"
    author = "omoika"
    description = "Represent an automobile."

    elements = [
        TextInput(label="VIN", icon="hash"),
        TextInput(label="Registration", icon="hash"),
        TextInput(label="Make", icon="tool"),
        TextInput(label="Model", icon="tools"),
    ]

