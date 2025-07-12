from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes  # This imports your routes after bp is defined
