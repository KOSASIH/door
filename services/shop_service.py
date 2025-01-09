# services/shop_service.py

import logging

logger = logging.getLogger(__name__)

class ShopService:
    def __init__(self):
        """
        Initialize the ShopService.
        """
        self.products = {}  # Dictionary to store products

    def add_product(self, product_id, product_info):
        """
        Add a new product to the shop.
        
        :param product_id: The ID of the product.
        :param product_info: A dictionary containing product details.
        """
        self.products[product_id] = product_info
        logger.info(f"Product added: {product_id}")

    def get_product(self, product_id):
        """
        Retrieve product information by product ID.
        
        :param product_id: The ID of the product.
        :return: The product information.
        """
        product = self.products.get(product_id)
        if product:
            logger.info(f"Retrieved product: {product_id}")
            return product
        else:
            logger.error("Product not found.")
            return None

    def process_transaction(self, product_id, user_id):
        """
        Process a transaction for a product purchase.
        
        :param product_id: The ID of the product being purchased.
        :param user_id: The ID of the user making the purchase.
        :return: A confirmation message.
        """
        if product_id in self.products:
            logger.info(f"Processing transaction for user {user_id} for product {product_id}.")
            # Here you would implement payment processing logic
            return f"Transaction successful for user {user_id} purchasing {product_id}."
        else:
            logger.error("Transaction failed: Product not found.")
            return "Transaction failed: Product not found."
