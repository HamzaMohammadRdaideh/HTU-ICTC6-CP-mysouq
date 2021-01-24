from mongoengine import *
from datetime import datetime
from . item import Item
from . user import User


class BuyRequest(Document):

    # define class metadata
    meta = {'collection' : 'buy_requests'}

    # define class fields    
    user = ReferenceField(User)
    item = ReferenceField(Item)
    status = StringField(required = True)


class UpgradeRequest(Document):

    # define class metadata
    meta = {'collection' : 'upgrade_requests'}    

    # define class fields    
    user = ReferenceField(User)
    status = StringField(required = True)        