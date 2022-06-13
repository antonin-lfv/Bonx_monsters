from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    level = db.Column(db.Integer)
    coins = db.Column(db.Integer)
    monsters = db.relationship('Monster', backref='user', lazy=True)

class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    level = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    power = db.Column(db.Integer)  # to calculate the level of the player
    rarity = db.Column(db.String(100))  # common, rare, epic, legendary
    img_path = db.Column(db.String(1000))
    amount = db.Column(db.Integer)  # number of this monster in the deck
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)