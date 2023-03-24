from flask import Flask, render_template, redirect, Blueprint, request, url_for, session, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from os.path import exists
from app import db
from models import User, Monster, Match
import random
from configuration.utils import *
from configuration.config import GameConfig

from configuration.utils import all_monsters_from_json, create_and_add_new_match_in_history, \
    create_and_add_new_monster_from_json

BLP_general = Blueprint('BLP_general', __name__,
                        template_folder='templates',
                        static_folder='static')


@BLP_general.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    return render_template('general/index.html', name=current_user.name)


@BLP_general.route('/monsters', defaults={"rarity": "All"}, methods=['POST', 'GET'])
@BLP_general.route('/monsters/<string:rarity>/', methods=['POST', 'GET'])
@login_required
def monsters(rarity):
    monsters = all_monsters_from_json()
    # delete the first key of the dict monsters
    monsters.pop('meta')
    # filter monsters by rarity
    if rarity == "Legendary":
        monsters = {k: v for k, v in monsters.items() if v['rarity'] == "Legendary"}
    elif rarity == "Epic":
        monsters = {k: v for k, v in monsters.items() if v['rarity'] == "Epic"}
    elif rarity == "Rare":
        monsters = {k: v for k, v in monsters.items() if v['rarity'] == "Rare"}
    elif rarity == "Common":
        monsters = {k: v for k, v in monsters.items() if v['rarity'] == "Common"}

    return render_template('general/monsters.html', monsters=monsters, len=len, int=int, rarity=rarity)


@BLP_general.route('/monster_details/<name_monster>', methods=['POST', 'GET'])
@login_required
def monster_details(name_monster):
    """
    Monsters of the user
    """
    monster = Monster.query.filter_by(user_id=current_user.id, name=name_monster).first()
    return render_template('general/monster_details.html', monster=monster, GameConfig=GameConfig)


@BLP_general.route('/monster_details_inventory/<name_monster>', methods=['POST', 'GET'])
@login_required
def monster_details_inventory(name_monster):
    """
    All monsters
    """
    monster = all_monsters_from_json()[name_monster]
    return render_template('general/monster_details_inventory.html', monster=monster, name=name_monster,
                           GameConfig=GameConfig)


@BLP_general.route('/match_history', methods=['POST', 'GET'])
@login_required
def match_history():
    ten_last_games_history = Match.query.filter_by(user_id=current_user.id).order_by(Match.id.desc()).limit(10).all()
    opponents = []
    for game in ten_last_games_history:
        opponents.append(Monster.query.filter_by(name=game.opponent).first())
    return render_template('general/match_history.html', games_history=ten_last_games_history, opponents=opponents,
                           zip=zip)


@BLP_general.route('/battle', methods=['POST', 'GET'])
@login_required
def battle():
    """
    Page to choose the opponent
    :return:
    """
    return render_template('general/battle.html')


@BLP_general.route('/game_page/<string:opponent>/', methods=['POST', 'GET'])
@login_required
def game_page(opponent):
    """
    Page to fight
    :param opponent: name of the opponent
    """
    # Get all the bosses
    bosses = all_bosses_from_json()
    # Get the users' monsters to display them in the game page to choose the monsters to fight with
    monsters = Monster.query.filter_by(user_id=current_user.id).all()
    if opponent in bosses.keys():
        # We fight a boss
        return render_template('general/game_page.html',
                               opponent=opponent,
                               boss_info=[bosses[opponent]],
                               monsters=monsters)
    else:
        # We fight in a dungeon
        ...


@BLP_general.route('/profil', defaults={'rarity': 'All'}, methods=['POST', 'GET'])
@BLP_general.route('/profil/<string:rarity>/', methods=['POST', 'GET'])
@login_required
def profil(rarity):
    # ===== add some monsters
    """for monster_name, _ in all_monsters_from_json().items():
        if monster_name != "meta":
            create_and_add_new_monster_from_json(monster_name, current_user.id)"""

    # ===== add some matches
    create_and_add_new_match_in_history(id_user=current_user.id, opponent="Lord bacus", reward_coin=10000, win="y")

    # get Legendary monsters
    legendary_monsters = Monster.query.filter_by(user_id=current_user.id, rarity="Legendary").all()
    # get Epic monsters
    epic_monsters = Monster.query.filter_by(user_id=current_user.id, rarity="Epic").all()
    # get Rare monsters
    rare_monsters = Monster.query.filter_by(user_id=current_user.id, rarity="Rare").all()
    # get Common monsters
    common_monsters = Monster.query.filter_by(user_id=current_user.id, rarity="Common").all()
    # get all monsters filtered by rarity selected
    if rarity == "Legendary":
        monsters = legendary_monsters
    elif rarity == "Epic":
        monsters = epic_monsters
    elif rarity == "Rare":
        monsters = rare_monsters
    elif rarity == "Common":
        monsters = common_monsters
    else:
        monsters = legendary_monsters + epic_monsters + rare_monsters + common_monsters

    return render_template('general/profil.html', user=current_user, monsters=monsters, len=len, int=int, rarity=rarity)


@BLP_general.route('/shop', methods=['POST', 'GET'])
@login_required
def shop():
    """
    Page to buy monsters
    """
    # update shop if needed
    update_shop()
    # get all the monsters in the shop
    shop_monsters = ShopItem.query.all()
    return render_template('general/shop.html', shop_monsters=shop_monsters, GameConfig=GameConfig)


@BLP_general.route('/about', methods=['POST', 'GET'])
@login_required
def about():
    return render_template('general/about.html')


@BLP_general.route('/get_monster_stats/<string:name>/', methods=['POST', 'GET'])
@login_required
def get_monster_stats(name):
    """
    Get the stats of a monster
    :param name: name of the monster
    :return: json with the stats
    """
    # replace underscore by space in the name
    name = name.replace("_", " ")
    # get the monster
    monster = Monster.query.filter_by(user_id=current_user.id, name=name).first()
    # create a dict with the stats
    stats = {"name": monster.name,
             "rarity": monster.rarity,
             "level": monster.level,
             "attack": monster.attack,
             "defense": monster.defense,
             "img_path": monster.img_path}

    # return the dict as json
    return jsonify(stats)


# ====== API ======

@BLP_general.route('/api/get_user_coins', methods=['GET', 'POST'])
@login_required
def get_user_coins():
    """
    Get the number of coins of the user
    :return: json with the number of coins
    """
    # get the number of coins
    coins = User.query.filter_by(id=current_user.id).first().coins
    # return the number of coins as json
    return jsonify({"coins": coins})


@BLP_general.route('/api/buy_monster/<string:name>/', methods=['POST', 'GET'])
@login_required
def buy_monster(name):
    """
    Buy a monster
    :param name: name of the monster
    :return: json with the result of the transaction
    """
    # replace underscore by space in the name
    name = name.replace("_", " ")
    # get the number of coins of the user
    coins = User.query.filter_by(id=current_user.id).first().coins
    # get the monster in json
    monster = all_monsters_from_json()[name]
    # get the rarity of the monster
    rarity = monster["rarity"]
    # get the price of the monster
    price = GameConfig.SHOP_CONFIG[rarity]["Price"]
    # Max card buyable per day
    max_buy = GameConfig.SHOP_CONFIG[rarity]["Max_per_day"]
    # user number of monsters bought
    user_bought = ShopItem.query.filter_by(monster_name=name).first().monster_bought
    # Get the monster in user monsters
    user_monster = Monster.query.filter_by(user_id=current_user.id, name=name).first()
    if user_monster:
        level = user_monster.level
    else:
        level = 0
    # if the user has already the monster
    if coins >= price and user_bought < max_buy and level < GameConfig.MAX_MONSTER_LEVEL:
        # remove the price of the monster from the number of coins of the user
        current_user.coins -= price
        # add 1 to amount of monsters bought
        ShopItem.query.filter_by(monster_name=name).first().monster_bought += 1
        # commit the changes
        db.session.commit()
        # add the monster to the user's monsters
        create_and_add_new_monster_from_json(name, current_user.id)
        # return the result of the transaction as json
        return jsonify({"result": "success"})
    else:
        # return the result of the transaction as json
        if user_bought >= max_buy:
            return jsonify({"result": "You bought the max number of this monster today"})
        elif level == GameConfig.MAX_MONSTER_LEVEL:
            return jsonify({"result": "You already have the max level of this monster"})
        elif coins < price:
            return jsonify({"result": "You don't have enough coins"})
        else:
            return jsonify({"result": "Error while buying the monster"})


@BLP_general.route('/api/get_last_update_shop', methods=['GET', 'POST'])
@login_required
def get_last_update_shop():
    """
    Get the last update of the shop
    :return: json with the last update of the shop
    """
    # get the last update of the shop
    last_update = ShopItem.query.first().last_update
    # return the last update of the shop as json
    return jsonify({"last_update_shop": last_update})


@BLP_general.route('/api/get_number_bought_monster/<string:name>/', methods=['POST', 'GET'])
@login_required
def get_number_bought_monster(name):
    """
    Get the number of a monster bought by the user
    :param name: name of the monster
    :return: json with the number of the monster bought by the user
    """
    # replace underscore by space in the name
    name = name.replace("_", " ")
    # get the number of the monster bought by the user
    number_bought = ShopItem.query.filter_by(monster_name=name).first().monster_bought
    # return the number of the monster bought by the user as json
    return jsonify({"number_bought": number_bought})
