# app/__init__.py
from flask import Flask
from .extensions import db, login_manager, migrate
from .auth import bp as auth_bp
from .main import bp as main_bp
from .admin import bp as admin_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app