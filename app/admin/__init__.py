# app/admin/__init__.py

from flask import Blueprint

bp = Blueprint('admin', __name__)

# Import routes after blueprint is defined to prevent circular imports
from . import routes
