#!/usr/bin/env python3
""" Flask Application """
from os import environ
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """app config class"""
    LANGUAGES = ["en", "fr"]

    def __init__(self):
        """init default values"""
        self.BABEL_DEFAULT_LOCALE = "en"
        self.BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config())


@app.route("/")
def index():
    """home page"""
    return render_template("0-index.html")


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
