import json
from app import db
from models import User, Monster, Match
from configuration.config import GameConfig


def all_monsters_from_json():
    with open('assets/bonx_data/monsters.json', 'r') as f:
        monsters = json.load(f)
    return monsters


def create_and_add_new_monster_from_json(monster_name, id_user):
    """Create and add monster if user don't already have it, else amount += 1"""
    if m := Monster.query.filter_by(user_id=id_user, name=monster_name).first():
        # if exists
        m.amount += 1
        if m.amount >= GameConfig.MONSTER_CONGIF[m.rarity]["Number of Cards to Upgrade"]:
            m.amount = 0
            m.level += 1
            m.defense *= round(GameConfig.MONSTER_CONGIF[m.rarity]["Ratio of Cards to Upgrade"], 1)
            m.attack *= round(GameConfig.MONSTER_CONGIF[m.rarity]["Ratio of Cards to Upgrade"], 1)
            m.power *= m.level
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


def create_and_add_new_match_in_history(id_user, opponent, reward_coin, win):
    """Add match in history + add coins in user wallet"""
    new_match = Match()
    new_match.opponent = opponent  # string
    new_match.reward_coin = reward_coin  # int
    new_match.win = win  # y or n
    new_match.user_id = id_user
    db.session.add(new_match)
    user = User.query.filter_by(id=id_user).first()
    user.coins += new_match.reward_coin
    user.coins = min(user.coins, GameConfig.MAX_COINS)  # max coins = 1 000 000
    db.session.commit()


def update_power_user(id_user):
    monsters = Monster.query.filter_by(user_id=id_user).all()
    user = User.query.filter_by(id=id_user).first()
    total_power = 0
    for m in monsters:
        total_power += m.power
    user.power = total_power
    db.session.commit()


def update_match_history_user(id_user):
    user = User.query.filter_by(id=id_user).first()
    history = Match.query.filter_by(user_id=id_user).all()
    user.nb_games = len(history)
    nb_wins = 0
    for m in history:
        if m.win == "y":
            nb_wins += 1
    user.nb_wins = nb_wins
    db.session.commit()
