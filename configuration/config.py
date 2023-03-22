
class Config(object):
    """
    Base config class
    """
    SECRET_KEY = "uYGBIUJKgUKYGkgukgFDjtfVUFTjJYgugGugYtfyuytfJY"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class GameConfig(Config):
    """
    Config class for the game
    MAX_COINS = 1000000
    COMMON_MONSTER_DEFENSE: defense of common monsters
    COMMON_MONSTER_ATTACK: attack of common monsters
    COMMON_MONSTER_POWER: power of common monsters
    COMMON_NUMBER_CARD_TO_UPGRADE: number of common cards to upgrade
    COMMON_RATIO_TO_UPGRADE: ratio of common cards to upgrade defense and attack
    RARE_MONSTER_DEFENSE: defense of rare monsters
    RARE_MONSTER_ATTACK: attack of rare monsters
    RARE_MONSTER_POWER: power of rare monsters
    RARE_NUMBER_CARD_TO_UPGRADE: number of rare cards to upgrade
    RARE_RATIO_TO_UPGRADE: ratio of rare cards to upgrade defense and attack
    EPIC_MONSTER_DEFENSE: defense of epic monsters
    EPIC_MONSTER_ATTACK: attack of epic monsters
    EPIC_MONSTER_POWER: power of epic monsters
    EPIC_NUMBER_CARD_TO_UPGRADE: number of epic cards to upgrade
    EPIC_RATIO_TO_UPGRADE: ratio of epic cards to upgrade defense and attack
    LEGENDARY_MONSTER_DEFENSE: defense of legendary monsters
    LEGENDARY_MONSTER_ATTACK: attack of legendary monsters
    LEGENDARY_MONSTER_POWER: power of legendary monsters
    LEGENDARY_NUMBER_CARD_TO_UPGRADE: number of legendary cards to upgrade
    LEGENDARY_RATIO_TO_UPGRADE: ratio of legendary cards to upgrade defense and attack
    """
    MAX_COINS = 1000000
    MAX_MONSTER_LEVEL = 200
    MONSTER_CONGIF = {
        "Common": {
            "Defense": 70,
            "Attack": 40,
            "Power": 100,
            "Number of Cards to Upgrade": 10,
            "Update defense": 1050,
            "Update attack": 200
        },
        "Rare": {
            "Defense": 90,
            "Attack": 50,
            "Power": 200,
            "Number of Cards to Upgrade": 20,
            "Update defense": 1250,
            "Update attack": 400
        },
        "Epic": {
            "Defense": 110,
            "Attack": 60,
            "Power": 300,
            "Number of Cards to Upgrade": 30,
            "Update defense": 1450,
            "Update attack": 600
        },
        "Legendary": {
            "Defense": 150,
            "Attack": 80,
            "Power": 500,
            "Number of Cards to Upgrade": 40,
            "Update defense": 1850,
            "Update attack": 1000
        }
    }
    SHOP_CONFIG = {
        "Common": {
            "Price": 1500,
            "Max_per_day": 5
        },
        "Rare": {
            "Price": 2000,
            "Max_per_day": 3
        },
        "Epic": {
            "Price": 4000,
            "Max_per_day": 2
        },
        "Legendary": {
            "Price": 6000,
            "Max_per_day": 1
        }
    }


app_config = Config
