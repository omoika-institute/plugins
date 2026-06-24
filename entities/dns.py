import json
import re
from omoika.elements import TextInput, DropdownInput
import omoika



class DNS(omoika.Plugin):
    version = "1.0.0"
    label = "DNS"
    category = "Network"
    color = "#88304E99"
    icon = "creative-commons-nd"
    description = "The Domain Name System translates domains into IPs"
    elements = [
        TextInput(label="Value", icon="file-description"),
        DropdownInput(label="Record Type", options=[
            { "label": "NS" },
            { "label": "A" },
            { "label": "AAAA" },
            { "label": "CNAME" },
            { "label": "MX" },
            { "label": "SOA" },
            { "label": "TXT" },
            { "label": "PTR" },
            { "label": "SRV" },
            { "label": "CERT" },
            { "label": "DCHID" },
            { "label": "DNAME" }
        ])
    ]


    author = ["OSIB", "Bugfest"]

 
