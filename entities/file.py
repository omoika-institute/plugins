import omoika
from omoika.elements import UploadFileInput, TextInput


class File(omoika.Plugin):
    version = "1.0.0"
    label = "File"
    category = "Documents"
    color = "#9CA3AF99"
    icon = "file"
    author = "omoika"
    description = "Attach a generic file and metadata."

    elements = [
        UploadFileInput(label="Attachment", icon="file"),
        TextInput(label="Description", icon="file-description"),
    ]

