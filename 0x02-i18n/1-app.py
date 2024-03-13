#!/usr/bin/env python3
""" Flask Application """
from os import environ
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """app config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config())
babel = Babel(app)


@app.route("/")
def index():
    """home page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
