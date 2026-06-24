import omoika
from omoika.elements import TextInput


class BankAccount(omoika.Plugin):
    version = "1.0.0"
    label = "Bank Account"
    category = ["Finance", "Identity"]
    color = "#06B6D499"
    icon = "building-bank"
    author = "omoika"
    description = "Represent a bank account identifier."

    elements = [
        TextInput(label="Account Number", icon="hash"),
        TextInput(label="IBAN", icon="hash"),
        TextInput(label="Bank Name", icon="building"),
    ]

