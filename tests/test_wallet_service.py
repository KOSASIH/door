# tests/test_wallet_service.py

import unittest
from services.wallet_service import WalletService

class TestWalletService(unittest.TestCase):
    def setUp(self):
        self.wallet_service = WalletService()

    def test_create_wallet(self):
        wallet = self.wallet_service.create_wallet("test_user")
        self.assertIsNotNone(wallet, "Wallet should be created.")
        self.assertEqual(wallet.owner, "test_user", "Wallet owner should match the provided username.")

    def test_deposit_funds(self):
        wallet = self.wallet_service.create_wallet("test_user")
        initial_balance = wallet.balance
        self.wallet_service.deposit(wallet.id, 100)
        self.assertEqual(wallet.balance, initial_balance + 100, "Balance should be updated after deposit.")

    def test_withdraw_funds(self):
        wallet = self.wallet_service.create_wallet("test_user")
        self.wallet_service.deposit(wallet.id, 200)
        self.wallet_service.withdraw(wallet.id, 100)
        self.assertEqual(wallet.balance, 100, "Balance should be updated after withdrawal.")

    def test_withdraw_insufficient_funds(self):
        wallet = self.wallet_service.create_wallet("test_user")
        with self.assertRaises(ValueError, msg="Insufficient funds should raise an error."):
            self.wallet_service.withdraw(wallet.id, 100)

if __name__ == '__main__':
    unittest.main()
