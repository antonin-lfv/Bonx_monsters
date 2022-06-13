from flask import Flask, render_template, redirect, Blueprint, request, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from os.path import exists
from app import db
from models import User, Monster

from configuration.utils import all_monsters_from_json, create_and_add_new_monster_from_json

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
    create_and_add_new_monster_from_json("Yellow wizard", current_user.id)
    create_and_add_new_monster_from_json("Red wizard", current_user.id)
    create_and_add_new_monster_from_json("Lord bacus", current_user.id)
    create_and_add_new_monster_from_json("Black mage", current_user.id)
    monsters = Monster.query.filter_by(user_id=current_user.id).all()
    return render_template('general/profile.html', user=current_user, monsters=monsters, len=len)