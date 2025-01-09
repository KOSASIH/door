# services/wallet_service.py

import logging
from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)

class WalletService:
    def __init__(self):
        """
        Initialize the WalletService.
        """
        self.wallets = {}  # Dictionary to store wallets
        self.encryption_key = Fernet.generate_key()  # Generate a new encryption key
        self.cipher = Fernet(self.encryption_key)

    def create_wallet(self, user_id):
        """
        Create a new wallet for a user.
        
        :param user_id: The ID of the user for whom the wallet is created.
        :return: The wallet address.
        """
        wallet_address = f"wallet_{user_id}"
        self.wallets[wallet_address] = {'balance': 0}
        logger.info(f"Wallet created for user {user_id}: {wallet_address}")
        return wallet_address

    def migrate_wallet(self, old_wallet_address, new_wallet_address):
        """
        Migrate a wallet from an old address to a new address.
        
        :param old_wallet_address: The old wallet address.
        :param new_wallet_address: The new wallet address.
        """
        if old_wallet_address in self.wallets:
            self.wallets[new_wallet_address] = self.wallets.pop(old_wallet_address)
            logger.info(f"Wallet migrated from {old_wallet_address} to {new_wallet_address}")
        else:
            logger.error("Old wallet address not found.")

    def encrypt_data(self, data):
        """
        Encrypt sensitive wallet data.
        
        :param data: The data to encrypt.
        :return: The encrypted data.
        """
        encrypted_data = self.cipher.encrypt(data.encode())
        logger.info("Data encrypted successfully.")
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """
        Decrypt sensitive wallet data.
        
        :param encrypted_data: The encrypted data to decrypt.
        :return: The decrypted data.
        """
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        logger.info("Data decrypted successfully.")
        return decrypted_data
