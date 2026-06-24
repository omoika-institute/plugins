import omoika
from omoika.elements import UploadFileInput


class PDF(omoika.Plugin):
    version = "1.0.0"
    label = "PDF Uploads"
    category = "Documents"
    color = '#7a1f1f99'
    icon = "file-type-pdf"
    author = "omoika"
    description = "Upload a PDF document for analysis or reference."

    # Single upload input restricted to PDFs
    elements = [
        UploadFileInput(label="Upload a PDF File", icon="file-type-pdf", accept="application/pdf"),
    ]

    # No transforms for now; this plugin acts as a container for attachments

