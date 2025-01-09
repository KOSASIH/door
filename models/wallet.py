# models/wallet.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

db = SQLAlchemy()
logger = logging.getLogger(__name__)

class Wallet(db.Model):
    __tablename__ = 'wallets'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the wallet
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to the user
    balance = db.Column(db.Float, default=0.0)  # Wallet balance
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of wallet creation
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp of last update

    user = db.relationship('User ', backref='wallets')  # Relationship to User model

    def __repr__(self):
        return f'<Wallet {self.id} for User {self.user_id}>'

    def deposit(self, amount):
        """
        Deposit an amount into the wallet.
        
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            logger.info(f"Deposited {amount} to wallet {self.id}. New balance: {self.balance}")
        else:
            logger.error("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw an amount from the wallet.
        
        :param amount: The amount to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            logger.info(f"Withdrew {amount} from wallet {self.id}. New balance: {self.balance}")
            return True
        else:
            logger.error("Withdrawal amount must be positive and less than or equal to the balance.")
            return False
