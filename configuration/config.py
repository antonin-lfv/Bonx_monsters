from flask import Flask, render_template, redirect, Blueprint, request, url_for
import requests
import sqlite3 as sl


class Config(object):
    """
    Base config class
    """
    SECRET_KEY = "uYGBIUJKgUKYGkgukgFDjtfVUFTjJYgugGugYtfyuytfJY"


app_config = Config