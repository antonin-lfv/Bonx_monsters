class Config(object):
    """
    Base config class
    """
    SECRET_KEY = "uYGBIUJKgUKYGkgukgFDjtfVUFTjJYgugGugYtfyuytfJY"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True  # False for production mode


class GameConfig(Config):
    """
    Config class for the game
    MAX_COINS = 1000000
    MAX_MONSTER_LEVEL = 200
    MONSTER_CONFIG = stats for each monster type
    SHOP_CONFIG = price and max number of cards per day
    BOSS_CONFIG = reward for each boss type
    REWARD_CONFIG = chance to get each card type
    DUNGON_MONSTER_AMOUNT = number of monsters in each dungeon
    GAME_SPEED = To multiply the number of cards earned in each dungeon and boss
    """
    USER_STARTING_COINS = 500000
    USER_STARTING_NUMBER_OF_MONSTERS = 6
    MAX_COINS = 100000000
    MAX_MONSTER_LEVEL = 300
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
            "Price": 2500,
            "Max_per_day": 20
        },
        "Rare": {
            "Price": 4500,
            "Max_per_day": 20
        },
        "Epic": {
            "Price": 100000,
            "Max_per_day": 20
        },
        "Legendary": {
            "Price": 250000,
            "Max_per_day": 20
        }
    }
    BOSS_CONFIG = {
        "Easy": {
            "Reward": 10000,
            "Cards_multiplier": 1,
        },
        "Medium": {
            "Reward": 100000,
            "Cards_multiplier": 2,
        },
        "Hard": {
            "Reward": 1000000,
            "Cards_multiplier": 3,
        }
    }
    REWARD_CONFIG = {
        "Common": {
            "chance_to_get": 0.5,
            "max_cards": 40,
        },
        "Rare": {
            "chance_to_get": 0.3,
            "max_cards": 30,
        },
        "Epic": {
            "chance_to_get": 0.1,
            "max_cards": 30,
        },
        "Legendary": {
            "chance_to_get": 0.1,
            "max_cards": 20,
        }
    }
    DUNGON_MONSTER_AMOUNT = 5
    GAME_SPEED = 10  # 1 for normal, 2 for fast, 4 for superfast


app_config = Config
