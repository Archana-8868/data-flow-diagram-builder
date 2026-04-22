from flask import Blueprint, request, jsonify
from datetime import datetime

ai_bp = Blueprint("ai_bp", __name__)

@ai_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Input is required"}), 400

    return jsonify({
        "status": "success",
        "input": data["input"],
        "generated_at": datetime.now().isoformat()
    })