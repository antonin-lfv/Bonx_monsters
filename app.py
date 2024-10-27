from configuration.config import app_config
from flask import Flask, render_template
from os import path
from extensions import (
    db,
    login_manager,
)  # Importer db et login_manager depuis extensions


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="assets")
    app.config.from_object(app_config)

    # Importer les blueprints après la création de l'application
    from auth.auth import BLP_auth
    from general.general import BLP_general

    app.register_blueprint(BLP_auth)
    app.register_blueprint(BLP_general)

    # Initialiser les extensions avec l'application
    db.init_app(app)
    login_manager.init_app(app)

    if not path.exists("db.sqlite"):
        with app.app_context():
            db.create_all()

    # Déplacer l'import de User ici pour éviter les imports circulaires
    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.errorhandler(404)
    def forbidden(error):
        return render_template("errors/404.html")

    return app


app = create_app()


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
