# app/auth/user_login.py

from flask_login import UserMixin
from app.models import User

class UserLogin(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.email = user_data['email']

# This tells Flask-Login how to get a user from the DB
def user_loader(user_id):
    user = User.find_by_id(user_id)
    return UserLogin(user) if user else None
