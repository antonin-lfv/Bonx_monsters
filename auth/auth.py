from config import *

BLP_auth = Blueprint('BLP_auth', __name__,
                     template_folder='templates',
                     static_folder='static')


@BLP_auth.route('/login')
def login():
    return render_template('auth/login.html')


@BLP_auth.route('/view/<int:user_id>')
def signup(user_id):
    return render_template('auth/signup.html', product=user_id)
