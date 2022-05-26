from configuration.db import *

from auth.auth import BLP_auth
from general.general import BLP_general

# ===== Flask app
app = Flask(__name__, template_folder='templates', static_folder='assets')
app.config.from_object(app_config)
# ===== Blueprint
app.register_blueprint(BLP_auth)
app.register_blueprint(BLP_general)
# ===== database creation if empty
create_user_db()


# ===== error page
@app.errorhandler(404)
def forbidden(error):
    return render_template('errors/404.html')
