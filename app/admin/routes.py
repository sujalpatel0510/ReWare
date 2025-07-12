from flask import render_template
from flask_login import login_required
from app.admin import bp

@bp.route('/admin')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')  # Create this HTML later
