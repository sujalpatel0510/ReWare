from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import bp

@bp.route('/')
def landing():
    """Landing page accessible to all users"""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('main/landing.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    """Protected dashboard route"""
    return render_template('main/dashboard.html', 
                         user=current_user,
                         title="Dashboard")