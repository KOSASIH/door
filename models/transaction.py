# models/transaction.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

db = SQLAlchemy()
logger = logging.getLogger(__name__)

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the transaction
    wallet_id = db.Column(db.Integer, db.ForeignKey('wallets.id'), nullable=False)  # Foreign key to the wallet
    amount = db.Column(db.Float, nullable=False)  # Transaction amount
    transaction_type = db.Column(db.String(10), nullable=False)  # Type of transaction (e.g., 'deposit', 'withdraw')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of transaction creation

    wallet = db.relationship('Wallet', backref='transactions')  # Relationship to Wallet model

    def __repr__(self):
        return f'<Transaction {self.id} for Wallet {self.wallet_id}>'

    @classmethod
    def create_transaction(cls, wallet_id, amount, transaction_type):
        """
        Create a new transaction.
        
        :param wallet_id: The ID of the wallet associated with the transaction.
        :param amount: The amount of the transaction.
        :param transaction_type: The type of transaction ('deposit' or 'withdraw').
        :return: The created Transaction object.
        """
        transaction = cls(wallet_id=wallet_id, amount=amount, transaction_type=transaction_type)
        logger.info(f"Transaction created: {transaction}")
        return transaction
