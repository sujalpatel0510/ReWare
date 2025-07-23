from flask import Blueprint, request, jsonify
from app import bcrypt
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    User.create(data['username'], data['email'], hashed)
    return jsonify({"message": "User registered successfully"}), 201
