import json
from app import db
from models import User, Monster, Match, ShopItem
from configuration.config import GameConfig
import math
import random
from datetime import datetime


def all_monsters_from_json():
    with open('assets/bonx_data/monsters.json', 'r') as f:
        monsters = json.load(f)
    return monsters


def all_bosses_from_json():
    with open('assets/bonx_data/opponent.json', 'r') as f:
        bosses = json.load(f)
    return bosses


def create_and_add_new_monster_from_json(monster_name, id_user):
    """Create and add monster if user don't already have it, else amount += 1"""
    if m := Monster.query.filter_by(user_id=id_user, name=monster_name).first():
        # if exists
        m.amount += 1
        if m.amount >= GameConfig.MONSTER_CONGIF[m.rarity]["Number of Cards to Upgrade"] and \
                m.level < GameConfig.MAX_MONSTER_LEVEL:
            # if monster can be upgraded, so if amount >= number of cards to upgrade and level < max level
            levels_to_add = m.amount // GameConfig.MONSTER_CONGIF[m.rarity]["Number of Cards to Upgrade"]
            m.level += levels_to_add
            m.level = min(m.level, GameConfig.MAX_MONSTER_LEVEL)
            m.defense = int(math.sqrt(m.level) * GameConfig.MONSTER_CONGIF[m.rarity]["Update defense"] +
                            GameConfig.MONSTER_CONGIF[m.rarity]["Defense"])
            m.attack = int(math.sqrt(m.level) * GameConfig.MONSTER_CONGIF[m.rarity]["Update attack"] +
                           GameConfig.MONSTER_CONGIF[m.rarity]["Attack"])
            m.power = GameConfig.MONSTER_CONGIF[m.rarity]["Power"] * m.level
            m.amount = m.amount % GameConfig.MONSTER_CONGIF[m.rarity]["Number of Cards to Upgrade"]
        if m.level == GameConfig.MAX_MONSTER_LEVEL:
            # if monster is max level
            m.amount = GameConfig.MONSTER_CONGIF[m.rarity]["Number of Cards to Upgrade"]
        db.session.commit()
    else:
        # if not exists in db => create and add
        monsters = all_monsters_from_json()
        new_monster = Monster()
        new_monster.name = monster_name
        new_monster.level = 1
        new_monster.amount = 1
        new_monster.rarity = monsters[monster_name]["rarity"]
        new_monster.img_path = monsters[monster_name]["img_path"]
        new_monster.description = monsters[monster_name]["description"]
        new_monster.defense = GameConfig.MONSTER_CONGIF[new_monster.rarity]["Defense"]
        new_monster.attack = GameConfig.MONSTER_CONGIF[new_monster.rarity]["Attack"]
        new_monster.power = GameConfig.MONSTER_CONGIF[new_monster.rarity]["Power"]
        new_monster.user_id = id_user
        db.session.add(new_monster)
        db.session.commit()
    update_power_user(id_user)


def create_and_add_new_match_in_history(id_user, opponent, reward_coin, win):
    """
    Add match in history + add coins in user wallet
    """
    new_match = Match()
    new_match.opponent = opponent  # string
    new_match.reward_coin = reward_coin  # int
    new_match.win = win  # y or n
    new_match.user_id = id_user
    db.session.add(new_match)
    user = User.query.filter_by(id=id_user).first()
    user.coins += new_match.reward_coin
    user.coins = min(user.coins, GameConfig.MAX_COINS)
    # update nb games and nb wins of user
    history = Match.query.filter_by(user_id=id_user).all()
    user.nb_games = len(history)
    nb_wins = 0
    for m in history:
        if m.win == "y":
            nb_wins += 1
    user.nb_wins = nb_wins
    db.session.commit()
    # update power of user
    update_power_user(id_user)


def update_power_user(id_user):
    """
    Update the power of the user
    :param id_user: id of the user
    """
    monsters = Monster.query.filter_by(user_id=id_user).all()
    user = User.query.filter_by(id=id_user).first()
    total_power = 0
    for m in monsters:
        total_power += m.power
    user.power = total_power
    db.session.commit()


def update_shop():
    """
    If the shop last_update is older than 1 day, update it
    so update the shop with 6 new monsters and change the last_update
    """
    shop = ShopItem.query.all()
    if len(shop) == 0 or (datetime.now() - shop[0].last_update).days >= 1:
        # delete all shop items
        for s in shop:
            db.session.delete(s)
        # if shop is empty or if last_update is older than 1 day
        monsters_json = all_monsters_from_json()
        # get 6 random monsters names from monsters.json
        monster_names_to_add = random.sample(list(monsters_json.keys()), 6)
        for m in monster_names_to_add:
            new_shop_item = ShopItem()
            new_shop_item.monster_name = m
            new_shop_item.monster_img_path = monsters_json[m]["img_path"]
            new_shop_item.monster_rarity = monsters_json[m]["rarity"]
            new_shop_item.price = GameConfig.SHOP_CONFIG[monsters_json[m]["rarity"]]["Price"]
            new_shop_item.last_update = datetime.now()
            new_shop_item.monster_bought = 0
            db.session.add(new_shop_item)
            db.session.commit()
