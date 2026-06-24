import omoika
from omoika.elements import TextInput


class CompanyProfile(omoika.Plugin):
    version = "1.0.0"
    label = "Company Profile"
    category = ["Organizations", "Documents"]
    color = "#F59E0B99"
    icon = "building"
    author = "omoika"
    description = "Store basic company/organization details."

    elements = [
        TextInput(label="Company", icon="building"),
        TextInput(label="Domain", icon="world-www"),
        TextInput(label="Country", icon="flag"),
    ]

