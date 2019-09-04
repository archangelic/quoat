from datetime import datetime

import flask
from peewee import *

db = SqliteDatabase('quotes.db')

class QuotemealMeta(Model):
    class Meta:
        database = db

class User(QuotemealMeta):
    name = CharField()

class Quote(QuotemealMeta):
    text = TextField()
    submitted = DateTimeField(default=datetime.now)
    author = ForeignKeyField(User, backref='quotes')

db.create_tables([User, Quote])