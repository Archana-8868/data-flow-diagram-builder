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

@ai_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "input" not in data:
        return jsonify({"error": "Input is required"}), 400

    return jsonify({
        "recommendations": [
            {
                "action_type": "Optimize",
                "description": "Improve system performance and speed.",
                "priority": "High"
            },
            {
                "action_type": "Security",
                "description": "Protect user data and strengthen login security.",
                "priority": "Medium"
            },
            {
                "action_type": "Monitoring",
                "description": "Track system activity and logs regularly.",
                "priority": "Low"
            }
        ]
    })