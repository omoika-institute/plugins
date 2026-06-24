import omoika
from omoika.elements import TextAreaInput


class Unknown(omoika.Plugin):
    version = "1.0.0"
    label = "Unknown"
    category = "Generic"
    color = "#D1D5DB99"
    icon = "question-mark"
    author = "omoika"
    description = "Placeholder for unknown/unspecified entities."

    elements = [
        TextAreaInput(label="Notes", icon="notes"),
    ]

