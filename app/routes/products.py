# app/routes/products.py

from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Product  # ✅ Correct model name

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/')
@login_required
def product_listing():
    items = Product.query.all()
    return render_template('listing.html', products=items)
