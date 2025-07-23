from flask import Blueprint, request, jsonify
from app.models import AdminLog

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/log', methods=['POST'])
def log_admin_action():
    data = request.json
    AdminLog.log(
        data['adminId'],
        data['action'],
        data.get('targetUserId'),
        data.get('targetProductId'),
        data.get('reason', "")
    )
    return jsonify({"message": "Action logged."})
