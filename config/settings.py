# config/settings.py

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# General Settings
DEBUG = os.getenv("DEBUG", "False") == "True"  # Set to True for development
HOST = os.getenv("HOST", "0.0.0.0")  # Host for the application
PORT = int(os.getenv("PORT", 5000))  # Port for the application

# Database Settings
DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://username:password@localhost:5432/door_for_pi")

# JWT Settings
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")

# CORS Settings
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "*").split(",")  # Comma-separated list of allowed origins

# Logging Settings
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
