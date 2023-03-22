from flask import Flask, render_template, redirect, Blueprint, request, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from os.path import exists
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from app import db

BLP_auth = Blueprint('BLP_auth', __name__,
                     template_folder='templates',
                     static_folder='static')


@BLP_auth.route('/')
@BLP_auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (email := request.form.get("login_email")) and (password := request.form.get("login_password")):
            user = User.query.filter_by(email=email).first()
            # if user already exists
            if not user or not check_password_hash(user.password, password):
                return render_template('auth/login.html', wrong_credentials=True)
            login_user(user)
            return redirect(url_for('BLP_general.home'))
    return render_template('auth/login.html', wrong_credentials=False)


@BLP_auth.route('/signup', methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        if (email := request.form.get("signup_email")) and (password := request.form.get("signup_password")) and (
        name := request.form.get("signup_name")):
            user = User.query.filter_by(email=email).first()
            # if user already exists
            if user:
                return render_template('auth/registration.html', already_exists=True)
            # else - creation of the user
            new_user = User()
            new_user.email = email
            new_user.name = name
            new_user.password = generate_password_hash(password, method='sha256')
            new_user.level = 0
            new_user.coins = 0
            new_user.nb_games = 0
            new_user.nb_wins = 0
            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()
            return render_template('auth/login.html', wrong_credentials=False)
    return render_template('auth/registration.html', already_exists=False)


@BLP_auth.route('/logout', methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('BLP_auth.login'))
