from flask import Flask, render_template, redirect, Blueprint, request, url_for, session
from flask_login import LoginManager
from itsdangerous import URLSafeTimedSerializer
import requests
import sqlite3 as sl
from os.path import exists


class Config(object):
    """
    Base config class
    """
    SECRET_KEY = "uYGBIUJKgUKYGkgukgFDjtfVUFTjJYgugGugYtfyuytfJY"


app_config = Config