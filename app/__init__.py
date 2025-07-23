# app/__init__.py

from flask import Flask
from .extensions import db, login_manager, migrate, bcrypt
from .auth import bp as auth_bp
from .main import bp as main_bp
from .admin import bp as admin_bp
from .routes.products import products_bp  # ✅ import products blueprint
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'

    # user_loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(products_bp)  # ✅ register products blueprint

    return app
