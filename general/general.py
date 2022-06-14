from flask import Flask, render_template, redirect, Blueprint, request, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from os.path import exists
from app import db
from models import User, Monster

from configuration.utils import all_monsters_from_json, create_and_add_new_monster_from_json

BLP_general = Blueprint('BLP_general', __name__,
                        template_folder='templates',
                        static_folder='static')

def update_power_user(id_user):
    monsters = Monster.query.filter_by(user_id=id_user).all()
    user = User.query.filter_by(id=id_user).first()
    total_power = 0
    for m in monsters:
        total_power+=m.power
    user.power = total_power
    db.session.commit()

@BLP_general.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    return render_template('general/index.html', name=current_user.name)

@BLP_general.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    user = User.query.filter_by(id=current_user.id).first()
    create_and_add_new_monster_from_json("Yellow wizard", current_user.id)
    create_and_add_new_monster_from_json("Red wizard", current_user.id)
    create_and_add_new_monster_from_json("Lord bacus", current_user.id)
    create_and_add_new_monster_from_json("Black mage", current_user.id)
    update_power_user(id_user=current_user.id)
    monsters = Monster.query.filter_by(user_id=current_user.id).all()
    return render_template('general/profile.html', user=current_user, monsters=monsters, len=len, int=int)

@BLP_general.route('/monster_details/<id_monster>', methods=['POST', 'GET'])
@login_required
def monster_details(id_monster):
    monster = Monster.query.filter_by(user_id=current_user.id, id=id_monster).first()
    print(monster)
    print(id_monster)
    print(monster.img_path)
    return render_template('general/monster_details.html', monster=monster)