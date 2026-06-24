import omoika
from omoika.elements import TextInput


class DrugDealer(omoika.Plugin):
    version = "1.0.0"
    label = "Drug Dealer"
    category = "Identity"
    color = "#F43F5E99"
    icon = "user-minus"
    author = "omoika"
    description = "Represent a suspected drug dealer."

    elements = [
        TextInput(label="Name", icon="user"),
        TextInput(label="Alias", icon="mask"),
        TextInput(label="Territory", icon="map"),
    ]

