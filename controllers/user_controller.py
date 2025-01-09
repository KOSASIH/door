# controllers/user_controller.py

from flask import Blueprint, request, jsonify
from models import db, User 
from flask_jwt_extended import create_access_token
import logging

logger = logging.getLogger(__name__)
user_bp = Blueprint('users', __name__)

class UserController:
    @user_bp.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.find_by_username(username) or User.find_by_email(email):
            logger.warning("User  already exists.")
            return jsonify({"msg": "User  already exists."}), 400

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        logger.info(f"User  registered: {username}")
        return jsonify({"msg": "User  registered successfully."}), 201

    @user_bp.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.find_by_username(username)
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            logger.info(f"User  logged in: {username}")
            return jsonify(access_token=access_token), 200
        else:
            logger.warning("Invalid username or password.")
            return jsonify({"msg": "Invalid username or password."}), 401

    @user_bp.route('/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get(user_id)
        if user:
            return jsonify({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "created_at": user.created_at
            }), 200
        else:
            logger.warning("User  not found.")
            return jsonify({"msg": "User  not found."}), 404
