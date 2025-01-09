# controllers/analytics_controller.py

from flask import Blueprint, jsonify
from models import db, Transaction
import logging

logger = logging.getLogger(__name__)
analytics_bp = Blueprint('analytics', __name__)

class AnalyticsController:
    @analytics_bp.route('/transactions/summary', methods=['GET'])
    def transaction_summary():
        transactions = Transaction.query.all()
        total_transactions = len(transactions)
        total_amount = sum(transaction.amount for transaction in transactions)

        logger.info("Transaction summary retrieved.")
        return jsonify({
            "total_transactions": total_transactions,
            "total_amount": total_amount
        }), 200
