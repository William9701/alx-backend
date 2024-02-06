#!/usr/bin/env python3
"""
Display the current time
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext
from datetime import datetime
import pytz

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


@babel.timezoneselector
def get_timezone():
    """Determine the best time zone for the user"""
    # Check if 'timezone' parameter is provided in the request URL
    if 'timezone' in request.args:
        timezone = request.args['timezone']
        try:
            # Validate if provided timezone is valid
            pytz.timezone(timezone)
            return timezone
        except pytz.UnknownTimeZoneError:
            pass

    # Check if user is logged in and has preferred timezone
    if g.user and g.user.get('timezone'):
        try:
            # Validate if user timezone is valid
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except pytz.UnknownTimeZoneError:
            pass

    # Default to UTC
    return 'UTC'


def get_current_time():
    """Get the current time based on the inferred time zone"""
    timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(timezone))
    return current_time.strftime('%b %d, %Y, %I:%M:%S %p')


@app.route('/')
def index():
    """Render index.html"""
    current_time = get_current_time()
    return render_template('8-index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
