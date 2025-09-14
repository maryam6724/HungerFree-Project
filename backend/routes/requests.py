from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Request, User

requests_bp = Blueprint("requests", __name__)

# -------------------------
# GET /requests → role-based
# -------------------------
@requests_bp.route("/requests", methods=["GET"])
@jwt_required()
def get_requests():
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user["id"]).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if user.role == "restaurant":
        requests_data = Request.query.filter_by(restaurant_id=user.id).all()
    elif user.role == "ngo":
        requests_data = Request.query.filter_by(ngo_id=user.id).all()
    else:
        return jsonify({"error": "Invalid role"}), 403

    result = [
        {
            "id": r.id,
            "food_item": r.food_item,
            "quantity": r.quantity,
            "status": r.status,
            "restaurant_id": r.restaurant_id,
            "ngo_id": r.ngo_id,
            "created_at": r.created_at
        }
        for r in requests_data
    ]

    return jsonify(result), 200

# -------------------------
# POST /requests → NGO creates request
# -------------------------
@requests_bp.route("/requests", methods=["POST"])
@jwt_required()
def create_request():
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user["id"]).first()

    if not user or user.role != "ngo":
        return jsonify({"error": "Only NGOs can create requests"}), 403

    data = request.get_json()
    new_request = Request(
        food_item=data.get("food_item"),
        quantity=data.get("quantity"),
        ngo_id=user.id,
        restaurant_id=data.get("restaurant_id")
    )

    db.session.add(new_request)
    db.session.commit()

    return jsonify({"message": "Request created successfully"}), 201

# -------------------------
# PUT /requests/<id> → Restaurant updates request status
# -------------------------
@requests_bp.route("/requests/<int:request_id>", methods=["PUT"])
@jwt_required()
def update_request(request_id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user["id"]).first()

    if not user or user.role != "restaurant":
        return jsonify({"error": "Only restaurants can update requests"}), 403

    req = Request.query.get(request_id)
    if not req or req.restaurant_id != user.id:
        return jsonify({"error": "Request not found or unauthorized"}), 404

    data = request.get_json()
    req.status = data.get("status", req.status)

    db.session.commit()

    return jsonify({"message": "Request updated successfully"}), 200
