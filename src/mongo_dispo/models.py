import datetime

from mongoengine import (DateTimeField, Document, EmailField, EmbeddedDocument,
                         EmbeddedDocumentField, IntField, ListField,
                         StringField)


class Order(EmbeddedDocument):
    customer = StringField(max_length=255)
    collection = StringField(max_length=255)
    delivery = StringField(max_length=255)
    price = StringField(max_length=50)
    customer_email = EmailField(max_length=255)
    order_number = IntField(max_length=50)


class Entry(Document):
    orders = ListField(EmbeddedDocumentField(Order))
    timestamp = DateTimeField(default=datetime.datetime.now())
    headline = StringField(max_length=255)
