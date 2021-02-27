import numpy as np
import json
import sys
import time
import os
import scipy.io as sio


import flask
from flask import Flask, render_template, Response, request, make_response
import flask_login
from flask import send_from_directory

from utils import utils


class flask_app(object):
    """docstring for flask_app."""

    def __init__(self, key, settings):
        super(flask_app, self).__init__()
        self.app = Flask(__name__)
        self.um = utils.misc()
        self.context = self.um.read_json(settings)
        self.users = self.context["users"]
        self.app.secret_key = key
        self.login_manager = flask_login.LoginManager()
        self.login_manager.init_app(self.app)
        self.login_manager.user_loader(self.user_loader)
        self.login_manager.unauthorized_handler(self.unauthorized_handler)
        self.login_manager.request_loader(self.request_loader)

        self.create_endpoints()

    def create_endpoints(self):
        self.app.add_url_rule("/", "index", self.index)
        self.app.add_url_rule("/login", "login", self.login, 
                              methods=['GET', 'POST'])

        self.app.add_url_rule("/logout", "logout", self.logout)

        self.app.view_functions['index'] = self.index
        self.app.view_functions['login'] = self.login
        self.app.view_functions['logout'] = self.logout


    def index(self):
        return render_template('index.html')
    
    def login(self):
        if flask.request.method == 'GET':
            return render_template("login.html")

        email = request.form.get('email', None)
        password = request.form.get('password', None)
        password = self.um.get_md5hash(password.encode('utf-8'))

        if email in self.users:
            if self.users[email]['password'] == password:
                user = User()
                user.id = email
                flask_login.login_user(user)
                return flask.redirect("/")
            else:
                return "wrong password"
        else:
            return "user not found"

        return 'Bad login'

    def logout(self):
        flask_login.logout_user()
        return flask.redirect("/")

    @flask_login.login_required
    def protected():
        return 'Logged in as: ' + flask_login.current_user.id

    def user_loader(self, email):
        if email not in self.users:
            return

        user = User()
        user.id = email
        return user

    def request_loader(self, request):
        email = request.form.get('email')
        if email not in self.users:
            return

        user = User()
        user.id = email
        user.is_authenticated = request.form['password'] == self.users[email]['password']

        return user

    def unauthorized_handler(self):
        return flask.redirect("/login")

class User(flask_login.UserMixin):
    # TODO: Implement this
    pass


if __name__ == '__main__':
    pass
