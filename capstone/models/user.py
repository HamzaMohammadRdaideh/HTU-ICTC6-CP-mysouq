from mongoengine import *
from datetime import datetime
from passlib.hash import pbkdf2_sha256
from bson import ObjectId

class User(Document):

    # define class metadata
    meta = {'collection' : 'user'}

    # define class fields
    username = StringField(required = True, unique= True)
    first_name = StringField(required = True)
    last_name = StringField(required = True)
    password = StringField(required=True)
    birthday = DateTimeField(required=True)
    email = EmailField(required=True , unique = True)
    favorite = ListField(StringField())
    role = IntField(default = 0)
    disable = BooleanField(default = False)
    maintenance = BooleanField(default = False) 

    # this method authenticates the user using credentials
    def authenticate(self, username, password):
    
        # username and password -> from the login form
        # self.username and self.password -> from the database
        if username == self.username and pbkdf2_sha256.verify(password, self.password):
            return True
        else:
            return False

    
    def encrypt_password(self, password):
        return pbkdf2_sha256.hash(password)        


    # this method changes the user password
    def change_password(self, current_password, new_password):
        if pbkdf2_sha256.verify(current_password, self.password):
            self.password = self.encrypt_password(new_password)


    # this method serializes the object into a JSON object
    def serialize(self):
        serialized = {
            "id": str(self.pk),
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': 'nice try :)!',
            'role': self.role,
            'email': self.email,
            'favorite': self.favorite,
            'maintenance' : self.maintenance,
            'disable': self.disable
        }

        return serialized


# class UserQuerySet(QuerySet):

    # def maintanence_mode(self):

    #     return self.filter(role = 0 and 1).update(maintenance = True)