# routes/__init__.py

from .user_routes import user_bp
from .wallet_routes import wallet_bp
from .shop_routes import shop_bp
from .analytics_routes import analytics_bp

__all__ = ['user_bp', 'wallet_bp', 'shop_bp', 'analytics_bp']
