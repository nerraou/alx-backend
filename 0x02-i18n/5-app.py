#!/usr/bin/env python3
""" Flask Application """
from os import environ
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get user by id"""
    try:
        login_as = request.args.get("login_as")
        if login_as is None:
            return None
        return users.get(int(login_as), None)
    except e:
        return None


class Config:
    """app config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config())
babel = Babel(app)


@babel.localeselector
def get_locale():
    """locale selector method"""
    return request.args.get("locale", "en")


@app.before_request
def before_request():
    """before request handler"""
    print(get_user())
    g.user = get_user()


@app.route("/")
def index():
    """home page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
