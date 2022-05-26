from configuration.config import *

BLP_auth = Blueprint('BLP_auth', __name__,
                     template_folder='templates',
                     static_folder='static')


@BLP_auth.route('/')
@BLP_auth.route('/login')
def login():
    return render_template('auth/login.html')


@BLP_auth.route('/signup')
def registration():
    return render_template('auth/registration.html')
