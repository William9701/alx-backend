#!/usr/bin/env python3
"""
Force locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the best match for the user's preferred languages"""
    # Check if 'locale' parameter is provided in the request URL
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # If not provided or not supported, resort to default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render index.html"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
