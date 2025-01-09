# routes/user_routes.py

from flask import Blueprint
from controllers import UserController

user_bp = Blueprint('users', __name__)

# User-related routes
user_bp.add_url_rule('/register', view_func=User Controller.register, methods=['POST'])
user_bp.add_url_rule('/login', view_func=User Controller.login, methods=['POST'])
user_bp.add_url_rule('/<int:user_id>', view_func=User Controller.get_user, methods=['GET'])
