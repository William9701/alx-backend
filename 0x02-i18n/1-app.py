#!/usr/bin/env python3
"""this is the flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import _

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def home():
    """Render index.html"""
    return render_template('1-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(debug=True)
