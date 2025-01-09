# controllers/shop_controller.py

from flask import Blueprint, request, jsonify
from models import db, Shop
import logging

logger = logging.getLogger(__name__)
shop_bp = Blueprint('shops', __name__)

class ShopController:
    @shop_bp.route('/create', methods=['POST'])
    def create_shop():
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')

        new_shop = Shop(name=name, description=description)
        db.session.add(new_shop)
        db.session.commit()

        logger.info(f"Shop created: {name}.")
        return jsonify({"msg": "Shop created successfully.", "shop_id": new_shop.id}), 201

    @shop_bp.route('/<int:shop_id>/add_product', methods=['POST'])
    def add_product(shop_id):
        data = request.get_json()
        product_id = data.get('product_id')
        product_info = data.get('product_info')

        shop = Shop.query.get(shop_id)
        if shop:
            shop.add_product(product_id, product_info)
            db.session.commit()
            logger.info(f"Product {product_id} added to shop {shop_id}.")
            return jsonify({"msg": "Product added successfully."}), 200
        else:
            logger.warning("Shop not found.")
            return jsonify({"msg": "Shop not found."}), 404

    @shop_bp.route('/<int:shop_id>/remove_product', methods=['POST'])
    def remove_product(shop_id):
        data = request.get_json()
        product_id = data.get('product_id')

        shop = Shop.query.get(shop_id)
        if shop:
            shop.remove_product(product_id)
            db.session.commit()
            logger.info(f"Product {product_id} removed from shop {shop_id}.")
            return jsonify({"msg": "Product removed successfully."}), 200
        else:
            logger.warning("Shop not found.")
            return jsonify({"msg": "Shop not found."}), 404
