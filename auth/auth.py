from configuration.config import *
from configuration.db import *

BLP_auth = Blueprint('BLP_auth', __name__,
                     template_folder='templates',
                     static_folder='static')


@BLP_auth.route('/')
@BLP_auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (email := request.form.get("login_email")) and (password := request.form.get("login_password")):
            with user_db:
                user = user_db.execute(f"SELECT id FROM USER WHERE USER.email = '{email}' AND USER.password = '{password}'")
            if user.fetchall():
                # Authenticated - add token in session & db
                token = user_db.execute(f"SELECT token FROM USER WHERE USER.email = '{email}'").fetchall()[0][0]
                print(token)
                session['token_user'] = token
                return redirect(url_for('BLP_general.home'))
    return render_template('auth/login.html')


@BLP_auth.route('/signup', methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        if (email := request.form.get("signup_email")) and (password := request.form.get("signup_password")) and (name := request.form.get("signup_name")):
            # check if user not already exists
            if not user_db.execute(f"SELECT id FROM USER WHERE USER.email = '{email}'").fetchall():
                # ajout
                token = URLSafeTimedSerializer(app_config.SECRET_KEY).dumps(email, salt='email-confirm-key')
                user_db.execute(f"""
                INSERT INTO USER (name, email, password, token, level)
                VALUES ('{name}', '{email}', '{password}', '{token}', 1)
                """)
                user_db.commit()
                return render_template('auth/login.html')

    return render_template('auth/registration.html')


@BLP_auth.route('/logout', methods=["GET", "POST"])
def logout():
    del session
    return redirect(url_for('BLP_auth.login'))
