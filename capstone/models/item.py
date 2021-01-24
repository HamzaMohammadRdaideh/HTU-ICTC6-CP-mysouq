from mongoengine import *
from datetime import datetime
from . request import BuyRequest 


class Item(Document):

    # define class metadata
    meta = {'collection' : 'item'}

    # define class fields
    title = StringField(required = True)
    description = StringField(required = True)
    date = DateTimeField(default = datetime.now())
    price = FloatField(required = True)
    sold = BooleanField(default = False)
    category = StringField(required = True)
    buy_request_list = ListField(StringField())
    hidden = BooleanField(default = False)