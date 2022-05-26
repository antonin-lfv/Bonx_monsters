from configuration.config import *

from auth.auth import BLP_auth
from general.general import BLP_general

app = Flask(__name__)

app.register_blueprint(BLP_auth)
app.register_blueprint(BLP_general)
