#!/usr/bin/env python3
""" Flask Application """
from os import environ
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """app config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config())
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """home page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    print("timezone", babel.default_timezone)
    print("timezone", babel.default_locale)
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
