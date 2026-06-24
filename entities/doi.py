import json
import re
from omoika.elements import TextInput, DropdownInput
import omoika

class DOI(omoika.Plugin):
    version = "1.0.0"
    label = "DOI"
    category = "Documents"
    color = "#fab60899"
    icon = "object-scan"
    description = "A a digital identifier of an object, any object; physical, digital, or abstract. DOIs solve a common problem: keeping track of things."
    elements = [
        TextInput(label="DOI", icon="file-description"),
    ]
