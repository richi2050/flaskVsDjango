import datetime

from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(Model):
    username: CharField(unique=True)
    email:  CharField(unique=True)
    password: CharField(max_length=120)
    joined_at: DateTimeField(default= datetime.datetime.now)

    class Meta():
        database = DATABASE
        order_by = ('-joined_at')
