# routes/shop_routes.py

from flask import Blueprint
from controllers import ShopController

shop_bp = Blueprint('shops', __name__)

# Shop-related routes
shop_bp.add_url_rule('/create', view_func=ShopController.create_shop, methods=['POST'])
shop_bp.add_url_rule('/<int:shop_id>/add_product', view_func=ShopController.add_product, methods=['POST'])
shop_bp.add_url_rule('/<int:shop_id>/remove_product', view_func=ShopController.remove_product, methods=['POST'])
