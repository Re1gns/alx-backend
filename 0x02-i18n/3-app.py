#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Configure Babel
babel = Babel(app)

# Define the list of supported languages
app.config['LANGUAGES'] = ["en", "fr"]

# Set the default locale
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

# Determine the user's preferred language
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index():
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)