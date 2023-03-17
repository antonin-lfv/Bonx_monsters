
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
            "Defense": 30,
            "Attack": 40,
            "Power": 500,
            "Number of Cards to Upgrade": 10,
            "Ratio to Upgrade": 1.2
        },
        "Rare": {
            "Defense": 40,
            "Attack": 50,
            "Power": 1000,
            "Number of Cards to Upgrade": 20,
            "Ratio to Upgrade": 1.25
        },
        "Epic": {
            "Defense": 50,
            "Attack": 60,
            "Power": 2000,
            "Number of Cards to Upgrade": 30,
            "Ratio to Upgrade": 1.3
        },
        "Legendary": {
            "Defense": 60,
            "Attack": 70,
            "Power": 3000,
            "Number of Cards to Upgrade": 40,
            "Ratio to Upgrade": 1.15
        }
    }


app_config = Config
