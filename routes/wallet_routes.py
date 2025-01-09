# routes/wallet_routes.py

from flask import Blueprint
from controllers import WalletController

wallet_bp = Blueprint('wallets', __name__)

# Wallet-related routes
wallet_bp.add_url_rule('/create', view_func=WalletController.create_wallet, methods=['POST'])
wallet_bp.add_url_rule('/<int:wallet_id>/deposit', view_func=WalletController.deposit, methods=['POST'])
wallet_bp.add_url_rule('/<int:wallet_id>/withdraw', view_func=WalletController.withdraw, methods=['POST'])
