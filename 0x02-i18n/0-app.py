#!/usr/bin/env python3
"""this is the flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('0-index.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(debug=True)