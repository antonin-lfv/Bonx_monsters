
class Config(object):
    """
    Base config class
    """
    SECRET_KEY = "uYGBIUJKgUKYGkgukgFDjtfVUFTjJYgugGugYtfyuytfJY"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


app_config = Config
