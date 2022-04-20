"""
Empty module docstring
"""
import os

from api import app
@app.route('/')
@app.route('/api')
def api_home() -> str:
    """
    Empty method docstring
    """

    return f"Hello from flask blog api! The environment is {os.environ['FLASK_ENV']}"