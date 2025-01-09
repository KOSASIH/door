# models/user.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

db = SQLAlchemy()
logger = logging.getLogger(__name__)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the user
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email address
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of user creation
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp of last update

    def __repr__(self):
        return f'<User  {self.username}>'

    def set_password(self, password):
        """
        Set the user's password after hashing it.
        
        :param password: The plain text password to hash.
        """
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)
        logger.info(f"Password set for user {self.username}")

    def check_password(self, password):
        """
        Check if the provided password matches the stored hashed password.
        
        :param password: The plain text password to check.
        :return: True if the password matches, False otherwise.
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

    @classmethod
    def find_by_username(cls, username):
        """
        Find a user by their username.
        
        :param username: The username to search for.
        :return: The User object if found, None otherwise.
        """
        user = cls.query.filter_by(username=username).first()
        logger.info(f"User  lookup for {username}: {'Found' if user else 'Not Found'}")
        return user

    @classmethod
    def find_by_email(cls, email):
        """
        Find a user by their email address.
        
        :param email: The email to search for.
        :return: The User object if found, None otherwise.
        """
        user = cls.query.filter_by(email=email).first()
        logger.info(f"User  lookup for {email}: {'Found' if user else 'Not Found'}")
        return user
