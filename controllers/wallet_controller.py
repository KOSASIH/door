# controllers/wallet_controller.py

from flask import Blueprint, request, jsonify
from models import db, Wallet
import logging

logger = logging.getLogger(__name__)
wallet_bp = Blueprint('wallets', __name__)

class WalletController:
    @wallet_bp.route('/create', methods=['POST'])
    def create_wallet():
        data = request.get_json()
        user_id = data.get('user_id')

        new_wallet = Wallet(user_id=user_id)
        db.session.add(new_wallet)
        db.session.commit()

        logger.info(f"Wallet created for user {user_id}.")
        return jsonify({"msg": "Wallet created successfully.", "wallet_id": new_wallet.id}), 201

    @wallet_bp.route('/<int:wallet_id>/deposit', methods=['POST'])
    def deposit(wallet_id):
        data = request.get_json()
        amount = data.get('amount')

        wallet = Wallet.query.get(wallet_id)
        if wallet:
            wallet.deposit(amount)
            db.session.commit()
            logger.info(f"Deposited {amount} to wallet {wallet_id}.")
            return jsonify({"msg": "Deposit successful.", "new_balance": wallet.balance}), 200
        else:
            logger.warning("Wallet not found.")
            return jsonify({"msg": "Wallet not found."}), 404

    @wallet_bp.route('/<int:wallet_id>/withdraw', methods=['POST'])
    def withdraw(wallet_id):
        data = request.get_json()
        amount = data.get('amount')

        wallet = Wallet.query.get(wallet_id)
        if wallet and wallet.withdraw(amount):
            db.session.commit()
            logger.info(f"Withdrew {amount} from wallet {wallet_id}.")
            return jsonify({"msg": "Withdrawal successful.", "new_balance": wallet.balance}), 200
        else:
            logger.warning("Withdrawal failed: Wallet not found or insufficient funds.")
            return jsonify({"msg": "Withdrawal failed: Wallet not found or insufficient funds."}), 404
