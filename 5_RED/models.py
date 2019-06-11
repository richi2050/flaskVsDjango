import datetime

from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('social.db')

#mixin = una clase que esta diseña con el unico proposito de agregar funcionalidad a otras clases
class User(UserMixin, Model):
    username: CharField(unique=True)
    email:  CharField(unique=True)
    password: CharField(max_length=120)
    joined_at: DateTimeField(default= datetime.datetime.now)

    class Meta():
        database = DATABASE
        order_by = ('-joined_at')
