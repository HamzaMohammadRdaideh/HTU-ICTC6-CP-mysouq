from mongoengine import *
from datetime import datetime

class Category(Document):

    # define class metadata
    meta = {'collection' : 'categories'}

    # define class fields
    category_list = ListField(StringField())

