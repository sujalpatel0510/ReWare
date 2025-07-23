# app/models.py

from app.extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # Add any relationships if needed

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    status = db.Column(db.String(50))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Swap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    offeredItemId = db.Column(db.Integer, db.ForeignKey('product.id'))
    requestedItemId = db.Column(db.Integer, db.ForeignKey('product.id'))
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(20), default='pending')
