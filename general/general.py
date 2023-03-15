from flask import Flask, render_template, redirect, Blueprint, request, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from os.path import exists
from app import db
from models import User, Monster, Match
from configuration.utils import *

from configuration.utils import all_monsters_from_json, create_and_add_new_match_in_history, \
    create_and_add_new_monster_from_json

BLP_general = Blueprint('BLP_general', __name__,
                        template_folder='templates',
                        static_folder='static')


@BLP_general.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    return render_template('general/index.html', name=current_user.name)


@BLP_general.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    # ===== add some monsters
    create_and_add_new_monster_from_json("Yellow wizard", current_user.id)
    create_and_add_new_monster_from_json("Red wizard", current_user.id)
    create_and_add_new_monster_from_json("Lord bacus", current_user.id)
    create_and_add_new_monster_from_json("Black mage", current_user.id)
    create_and_add_new_monster_from_json("Dark scorp", current_user.id)
    update_power_user(id_user=current_user.id)
    # ===== add some matches
    create_and_add_new_match_in_history(id_user=current_user.id, opponent="Lord bacus", reward_coin=10000, win="y")
    update_match_history_user(id_user=current_user.id)

    monsters = Monster.query.filter_by(user_id=current_user.id).all()
    return render_template('general/profile.html', user=current_user, monsters=monsters, len=len, int=int)


@BLP_general.route('/monsters', methods=['POST', 'GET'])
@login_required
def monsters():
    monsters = all_monsters_from_json()
    # delete the first key of the dict monsters
    monsters.pop('meta')
    return render_template('general/monsters.html', monsters=monsters, len=len, int=int)


@BLP_general.route('/monster_details/<name_monster>', methods=['POST', 'GET'])
@login_required
def monster_details(name_monster):
    monster = Monster.query.filter_by(user_id=current_user.id, name=name_monster).first()
    return render_template('general/monster_details.html', monster=monster)


@BLP_general.route('/monster_details_inventory/<name_monster>', methods=['POST', 'GET'])
@login_required
def monster_details_inventory(name_monster):
    monster = all_monsters_from_json()[name_monster]
    return render_template('general/monster_details_inventory.html', monster=monster, name=name_monster)


@BLP_general.route('/match_history', methods=['POST', 'GET'])
def match_history():
    ten_last_games_history = Match.query.filter_by(user_id=current_user.id).order_by(Match.id.desc()).limit(10).all()
    opponents = []
    for game in ten_last_games_history:
        # TODO créer les monstres contre qui se battre, et adapter leur niveau à celui du joueur
        opponents.append(Monster.query.filter_by(name=game.opponent).first())
    return render_template('general/match_history.html', games_history=ten_last_games_history, opponents=opponents,
                           zip=zip)


@BLP_general.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('general/about.html')
