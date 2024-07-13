from flask import Blueprint

# Create an instance of the Blueprint class
bp = Blueprint('main', __name__, url_prefix='/')

# Define a route for the main page
@bp.route("/")
def main():
    return "Calendar working"
