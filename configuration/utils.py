import json
from xxlimited import new
from app import db
from models import User, Monster

def all_monsters_from_json():
    with open('assets/bonx_data/monsters.json', 'r') as f:
        monsters = json.load(f)
    return monsters

def create_and_add_new_monster_from_json(monster_name, id_user):
    """Create and add monster if user don't already have it, else amount += 1"""
    if m := Monster.query.filter_by(user_id=id_user, name=monster_name).first():
        # if exists
        m.amount += 1
        db.session.commit()
    else:
        monsters = all_monsters_from_json()
        new_monster = Monster()
        new_monster.name = monster_name
        new_monster.level = monsters[monster_name]["level"]
        new_monster.defense = monsters[monster_name]["defense"]
        new_monster.attack = monsters[monster_name]["attack"]
        new_monster.power = monsters[monster_name]["power"]
        new_monster.rarity = monsters[monster_name]["rarity"]
        new_monster.img_path = monsters[monster_name]["img_path"]
        new_monster.amount = monsters[monster_name]["amount"]
        new_monster.user_id = id_user
        db.session.add(new_monster)
        db.session.commit()