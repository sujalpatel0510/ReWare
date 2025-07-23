# app/admin/routes.py

from flask import render_template, redirect, url_for, flash, request
from . import bp  # ✅ Correct: relative import of bp
from app.models import Product, User

from app.extensions import db
from flask_login import login_required

@bp.route('/')
@login_required
def admin_home():
    users = User.query.all()
    items = Item.query.all()
    return render_template('admin/admin.html', users=users, items=items)

@bp.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted.')
    return redirect(url_for('admin.admin_home'))

@bp.route('/delete_item/<int:item_id>', methods=['POST'])
@login_required
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('admin.admin_home'))
