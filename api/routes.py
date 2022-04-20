"""
routes
------

This module allows users to view, add, delete or update blog posts. It contains
the following routes:

    */ - Access the home or index page through a get request
    */api - Access the home or index page through a get request  
"""


import os

from api import app
import werkzeug


@app.errorhandler(werkzeug.exceptions.MethodNotAllowed)
def handle_bad_request(e):
    """Handles bad request calls to api endpoints
    
    Returns
    -------
    tuple: str, int
        The str tells the user of the illegal method and the int is the error code
        405
        
    """

    return 'The method is not allowed!', 405


@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def api_home() -> str:
    """Provides access the contents of the home or index page.

    This method gives the blogger access to the contents of the home or index page.
    It is called when a GET request is made to the '/' or '/api' route. It assumes
    that the 'FLASK_ENV' environment variable is set.

    Raises
    ------
    MethodNotAllowed
        If any other HTTP request apart from GET is made to / or /api.

    Returns
    -------
    str
        The text string 'Hello from flask blog api! The environment is <flask environment>'.
        The value can only be 'test', 'development' or production. 
    """

    return f"Hello from flask blog api! The environment is {os.environ['FLASK_ENV']}"