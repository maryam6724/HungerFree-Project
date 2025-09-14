from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Donation, User
from socketio_instance import socketio


donations_bp = Blueprint("donations", __name__)

@donations_bp.route("", methods=["POST"])
@jwt_required()
def add_donation():
    current_user_email = get_jwt_identity()
    user = User.query.filter_by(email=current_user_email).first()
    if not user or user.role != "restaurant":
        return jsonify({"error": "Only restaurants can add donations"}), 403

    data = request.get_json()
    donation = Donation(food_item=data.get("food_item"), quantity=data.get("quantity"), restaurant_id=user.id)
    db.session.add(donation)
    db.session.commit()
    socketio.emit('donation_update', {'message': 'Donation added'})
    return jsonify({"message": "Donation added successfully"}), 201


@donations_bp.route("", methods=["GET"])
@jwt_required()
def get_donations():
    current_user_email = get_jwt_identity()
    user = User.query.filter_by(email=current_user_email).first()

    if user.role == "restaurant":
        donations = Donation.query.filter_by(restaurant_id=user.id).all()
    elif user.role == "ngo":
        # Available donations + requested/accepted/completed by this NGO
        available = Donation.query.filter(Donation.status=="available").all()
        my_requests = Donation.query.filter(Donation.ngo_id==user.id, Donation.status.in_(["requested", "accepted", "completed"])).all()
        donations = available + my_requests
    else:
        return jsonify({"error": "Invalid role"}), 403

    return jsonify([{
        "id": d.id, "food_item": d.food_item, "quantity": d.quantity,
        "status": d.status, "restaurant_id": d.restaurant_id,
        "restaurant_name": d.restaurant.name if d.restaurant else None,
        "ngo_id": d.ngo_id, "ngo_name": d.ngo.name if d.ngo else None,
        "created_at": d.created_at
    } for d in donations]), 200


@donations_bp.route("/<int:donation_id>/request", methods=["PUT"])
@jwt_required()
def request_donation(donation_id):
    current_user_email = get_jwt_identity()
    user = User.query.filter_by(email=current_user_email).first()
    if user.role != "ngo":
        return jsonify({"error": "Only NGOs can request donations"}), 403

    donation = Donation.query.get(donation_id)
    if not donation or donation.status != "available":
        return jsonify({"error": "Donation not available"}), 400

    donation.status = "requested"
    donation.ngo_id = user.id
    db.session.commit()
    socketio.emit('donation_update', {'message': 'Donation requested'})
    return jsonify({"message": "Donation requested successfully"}), 200


@donations_bp.route("/<int:donation_id>", methods=["PUT"])
@jwt_required()
def update_donation(donation_id):
    current_user_email = get_jwt_identity()
    user = User.query.filter_by(email=current_user_email).first()
    if user.role != "restaurant":
        return jsonify({"error": "Only restaurants can update donations"}), 403

    donation = Donation.query.get(donation_id)
    if not donation or donation.restaurant_id != user.id:
        return jsonify({"error": "Donation not found or unauthorized"}), 404

    data = request.get_json()
    status = data.get("status")
    if status not in ["accepted", "completed"]:
        return jsonify({"error": "Invalid status"}), 400

    donation.status = status
    db.session.commit()
    socketio.emit('donation_update', {'message': 'Donation updated'})
    return jsonify({"message": "Donation updated successfully"}), 200
