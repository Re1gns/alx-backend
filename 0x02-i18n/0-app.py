#!/usr/bin/env python3
"""
This module contains a basic Flask application with a single route.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page.

    Returns:
        str: The rendered HTML page as a string.
    """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)