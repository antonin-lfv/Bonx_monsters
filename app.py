from configuration.config import app_config
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()


def create_app():
    # ===== Flask app
    app = Flask(__name__, template_folder='templates', static_folder='assets')
    app.config.from_object(app_config)
    # ===== Blueprint
    from auth.auth import BLP_auth
    from general.general import BLP_general
    app.register_blueprint(BLP_auth)
    app.register_blueprint(BLP_general)
    # ===== init SQLAlchemy
    db.init_app(app)
    if not path.exists("db.sqlite"):
        db.create_all(app=app)
    # ===== Login manager
    login_manager = LoginManager()
    login_manager.login_view = 'BLP_auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # ===== error page
    @app.errorhandler(404)
    def forbidden(error):
        return render_template('errors/404.html')

    return app


app = create_app()
