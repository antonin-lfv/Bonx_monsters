class Config(object):
    """
    Base config class
    """
    SECRET_KEY = "uYGBIUJKgUKYGkgukgFDjtfVUFTjJYgugGugYtfyuytfJY"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False  # False for production mode


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
    DUNGON_CONFIG = stats for each dungon
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
            "Price": 2500,
            "Max_per_day": 10
        },
        "Rare": {
            "Price": 4500,
            "Max_per_day": 5
        },
        "Epic": {
            "Price": 10000,
            "Max_per_day": 5
        },
        "Legendary": {
            "Price": 20000,
            "Max_per_day": 5
        }
    }
    BOSS_CONFIG = {
        "Easy": {
            "Reward": 5000,
        },
        "Medium": {
            "Reward": 35000,
        },
        "Hard": {
            "Reward": 75000,
        }
    }
    REWARD_CONFIG = {
        "Common": {
            "chance_to_get": 0.5,
            "max_cards": 10,
        },
        "Rare": {
            "chance_to_get": 0.3,
            "max_cards": 5,
        },
        "Epic": {
            "chance_to_get": 0.1,
            "max_cards": 5,
        },
        "Legendary": {
            "chance_to_get": 0.1,
            "max_cards": 5,
        }
    }
    DUNGON_MONSTER_AMOUNT = 5


app_config = Config
