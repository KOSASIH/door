# routes/analytics_routes.py

from flask import Blueprint
from controllers import AnalyticsController

analytics_bp = Blueprint('analytics', __name__)

# Analytics-related routes
analytics_bp.add_url_rule('/transactions/summary', view_func=AnalyticsController.transaction_summary, methods=['GET'])
