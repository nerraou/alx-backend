#!/usr/bin/env python3
""" Flask Application """
from os import environ
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

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
    languages = app.config["LANGUAGES"]

    if "locale" in request.args:
        locale = request.args.get("locale")
        if locale in languages:
            return locale

    if g.user is not None and g.user.get("locale", "") in languages:
        return g.user.get("locale")

    if "locale" in request.headers:
        locale = request.headers.get("locale", "")
        if locale in languages:
            return locale

    locale = request.accept_languages.best_match(languages)

    if locale is not None:
        return locale

    return app.config["BABEL_DEFAULT_LOCALE"]


@babel.timezoneselector
def get_timezone():
    """get timezone"""
    print("GET TIMEZONE")
    try:
        timezone = None

        if "timezone" in request.args:
            timezone = request.args.get("timezone")
        elif g.user is not None:
            timezone = g.user.get("timezone")

        pytz.timezone(timezone)
        return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.before_request
def before_request():
    """before request handler"""
    g.user = get_user()


@app.route("/")
def index():
    """home page"""
    return render_template("7-index.html")


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
