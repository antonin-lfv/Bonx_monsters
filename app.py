from configuration.config import *
from configuration.utils import *

from auth.auth import BLP_auth
from general.general import BLP_general

app = Flask(__name__, template_folder='templates')
app.config.from_object(app_config)


@app.errorhandler(404)
def forbidden(error):
    return render_template('errors/404.html')


app.register_blueprint(BLP_auth)
app.register_blueprint(BLP_general)
