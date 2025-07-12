from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes  # Make sure routes.py exists

