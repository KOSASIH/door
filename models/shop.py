# models/shop.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

db = SQLAlchemy()
logger = logging.getLogger(__name__)

class Shop(db.Model):
    __tablename__ = 'shops'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the shop
    name = db.Column(db.String(100), unique=True, nullable=False)  # Shop name
    description = db.Column(db.String(255))  # Shop description
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of shop creation
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp of last update

    def __repr__(self):
        return f'<Shop {self.name}>'

    def add_product(self, product_id, product_info ):
        """
        Add a product to the shop's inventory.
        
        :param product_id: The ID of the product to add.
        :param product_info: Information about the product.
        """
        # Logic to add the product to the shop's inventory
        logger.info(f"Product {product_id} added to shop {self.name}.")

    def remove_product(self, product_id):
        """
        Remove a product from the shop's inventory.
        
        :param product_id: The ID of the product to remove.
        """
        # Logic to remove the product from the shop's inventory
        logger.info(f"Product {product_id} removed from shop {self.name}.")
