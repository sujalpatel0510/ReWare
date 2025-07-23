from flask import Blueprint, request, jsonify
from app.models import Swap

swap_bp = Blueprint('swap', __name__)

@swap_bp.route('/swap', methods=['POST'])
def swap_request():
    data = request.json
    Swap.create(
        data['senderUserId'],
        data['receiverUserId'],
        data['offeredItemId'],
        data['requestedItemId'],
        data['message']
    )
    return jsonify({"message": "Swap requested."})
