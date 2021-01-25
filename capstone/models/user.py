from mongoengine import *
from datetime import datetime
from .item import Item
from passlib.hash import pbkdf2_sha256

class User(Document):

    # define class metadata
    meta = {'collection' : 'user'}

    # define class fields
    username = StringField(required = True, unique= True)
    password = StringField(required=True)
    brithday = DateTimeField(required=True)
    email = EmailField(required=True)
    favorite = ListField(StringField())
    role = IntField(default = 0)
    disable = BooleanField(default = False)


    def authenticate(self, username, password):
        # username / password -> from the login form
        # self.username / self.password -> from the database
        if username == self.username and password == self.password:
            return True
        else:
            return False

    
    def encrypt_password(self, password):
        return pbkdf2_sha256.hash(password)        





