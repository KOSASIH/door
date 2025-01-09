# tests/test_shop_service.py

import unittest
from services.shop_service import ShopService

class TestShopService(unittest.TestCase):
    def setUp(self):
        self.shop_service = ShopService()

    def test_add_product(self):
        product = self.shop_service.add_product("Test Product", "This is a test product.", 10.99)
        self.assertIsNotNone(product, "Product should be added successfully.")
        self.assertEqual(product.name, "Test Product", "Product name should match.")

    def test_get_all_products(self):
        self.shop_service.add_product("Test Product 1", "Description 1", 10.99)
        self.shop_service.add_product("Test Product 2", "Description 2", 15.99)
        products = self.shop_service.get_all_products()
        self.assertGreater(len(products), 0, "There should be products in the shop.")

if __name__ == '__main__':
    unittest.main()
