from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return "Error 404 page not found."

@main.app_errorhandler(500)
def internal_server_error(e):
    return "Server error has occurred visit after some time."
