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


@babel.localeselector
def get_locale():
    """Get the best language for the job"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """Render index.html"""
    return render_template('3-index.html', title=_(u'home_title'),
                           header=_(u'home_header'))


if __name__ == "__main__":
    """ Main Function """
    app.run(debug=True)
