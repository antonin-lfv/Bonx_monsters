from config import *

from auth.auth import BLP_auth
from general.general import BLP_general

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(BLP_auth)
app.register_blueprint(BLP_general)
