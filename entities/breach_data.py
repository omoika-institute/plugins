import omoika
from omoika.elements import TextInput, UploadFileInput


class BreachData(omoika.Plugin):
    version = "1.0.0"
    label = "Breach Data"
    category = ["Threat Intelligence", "Documents"]
    color = "#EF444499"
    icon = "database-exclamation"
    author = "omoika"
    description = "Reference breached data sources or upload small snippets."

    elements = [
        TextInput(label="Source", icon="database-search"),
        TextInput(label="Reference", icon="link"),
        UploadFileInput(label="Snippet", icon="file", accept="text/plain"),
    ]
