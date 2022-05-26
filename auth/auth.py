from configuration.config import *
from app import user_db

BLP_auth = Blueprint('BLP_auth', __name__,
                     template_folder='templates',
                     static_folder='static')


@BLP_auth.route('/')
@BLP_auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if email := request.form.get("login_email") and (password := request.form.get("login_password")):
            with user_db:
                user = user_db.execute(f"SELECT * FROM USER WHERE email == {email} AND password == {password}")
            if user is not None:
                # Authenticated - add token in session & db
                token = URLSafeTimedSerializer(app_config.SECRET_KEY).dumps(email, salt='email-confirm-key')
                session['token_user'] = token
                user_db.execute(f"""
                UPDATE USER
                SET token = {token}
                WHERE
                    email ==  {email}
                """)
                return redirect('general/index.html')
    return render_template('auth/login.html')


@BLP_auth.route('/signup')
def registration():
    return render_template('auth/registration.html')
