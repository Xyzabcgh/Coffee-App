from flask import Blueprint, request, jsonify
from firebase_config import db

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/check-user', methods=['POST'])
def check_user():
    phone_number = request.json.get('phone_number')
    try:
        users = db.child("users").get().val() or {}
        for user_id, user_data in users.items():
            if user_data.get('phone_number') == phone_number:
                return jsonify({"exists": True, "message": "User exists"}), 200
        return jsonify({"exists": False, "message": "User not found"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data = request.json
    phone_number = data.get('phone_number')
    email = data.get('email')
    username = data.get('username')

    try:
        user_data = {
            "phone_number": phone_number,
            "email": email,
            "username": username
        }
        db.child("users").push(user_data)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
