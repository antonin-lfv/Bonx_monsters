from configuration.importations import *
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    level = db.Column(db.Integer)


class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)