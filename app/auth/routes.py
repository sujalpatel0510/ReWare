# from flask import render_template, redirect, url_for, flash, request
# from flask_login import login_user, logout_user, current_user
# from app.auth import bp
# from app.auth.forms import LoginForm, RegistrationForm
# from app.models import User
# from app import db

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid email or password')
#             return redirect(url_for('auth.login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         return redirect(next_page or url_for('main.index'))
#     return render_template('auth/login.html', title='Sign In', form=form)

# @bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('auth.login'))
#     return render_template('auth/register.html', title='Register', form=form)

# @bp.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('main.index'))
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)
