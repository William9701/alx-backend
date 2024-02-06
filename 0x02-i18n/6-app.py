#!/usr/bin/env python3
"""
Use user locale
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """Set the logged-in user as a global variable"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


def get_user(user_id):
    """Retrieve user information based on user ID"""
    try:
        user_id = int(user_id)
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@babel.localeselector
def get_locale():
    """Determine the best match for the user's preferred languages"""
    # Check if 'locale' parameter is provided in the request URL
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale

    # Check if user is logged in and has preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Return locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render index.html"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
