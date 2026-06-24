import omoika
from omoika.elements import UploadFileInput, TextInput


class MetadataEXIF(omoika.Plugin):
    version = "1.0.0"
    label = "Metadata EXIF"
    category = "Documents"
    color = "#94A3B899"
    icon = "photo"
    author = "omoika"
    description = "Attach an image and record parsed EXIF fields."

    elements = [
        UploadFileInput(label="Image", icon="photo", accept="image/*"),
        TextInput(label="Camera", icon="camera"),
        TextInput(label="Timestamp", icon="calendar"),
        TextInput(label="GPS", icon="map-pin"),
    ]
