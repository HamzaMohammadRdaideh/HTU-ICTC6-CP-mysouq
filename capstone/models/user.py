from mongoengine import *
from datetime import datetime
from .item import Item

class User(Document):

    # define class metadata
    meta = {'collection' : 'user'}

    # define class fields
    username = StringField(required = True, unique= True)
    brithday = DateTimeField(required=True)
    email = EmailField(required=True)
    favorite = ListField(StringField())
    role = IntField(default = 0)
    disable = BooleanField(default = False)




