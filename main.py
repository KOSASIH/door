from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager
import logging
from config.constants import (
    DOOR_FOR_PI_VERSION,
    DOOR_FOR_PI_RELEASE_DATE,
    DATABASE_URI,
    JWT_SECRET_KEY,
)

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY  # Set JWT secret key

# Initialize extensions
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins for SocketIO
jwt = JWTManager(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import routes
from routes.user_routes import user_bp
from routes.wallet_routes import wallet_bp
from routes.shop_routes import shop_bp
from routes.analytics_routes import analytics_bp

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(wallet_bp, url_prefix='/api/wallets')
app.register_blueprint(shop_bp, url_prefix='/api/shops')
app.register_blueprint(analytics_bp, url_prefix='/api/analytics')

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Door for Pi API",
        "version": DOOR_FOR_PI_VERSION,
        "release_date": DOOR_FOR_PI_RELEASE_DATE
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal error: {error}")
    return jsonify({"error": "Internal server error"}), 500

@socketio.on('connect')
def handle_connect():
    logger.info("Client connected")
    socketio.emit('response', {'data': 'Connected to the Door for Pi server!'})

@socketio.on('disconnect')
def handle_disconnect():
    logger.info("Client disconnected")

if __name__ == '__main__':
    logger.info("Starting Door for Pi application...")
    socketio.run(app, host='0.0.0.0', port=5000)
