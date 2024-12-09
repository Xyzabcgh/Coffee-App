from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import User  # Assuming your User model is set up with MongoEngine

auth_bp = Blueprint('auth', __name__)

# Signup route
@auth_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check if user already exists
        if User.objects(username=username).first() or User.objects(email=email).first():
            return jsonify({"error": "User already exists"}), 409

        # Hash the password and create a new user
        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=hashed_password)
        user.save()

        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.objects(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"error": "Invalid email or password"}), 401

        # Generate JWT token for the authenticated user
        access_token = create_access_token(identity=str(user.id))  # identity can be the user ID

        return jsonify({
            "message": "Login successful",
            "access_token": access_token  # Send token in response
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Fetch user details route
@auth_bp.route('/user/details', methods=['GET'])
@jwt_required()  # Protect this route with JWT authentication
def get_user_details():
    try:
        # Get the user ID from the JWT token
        user_id = get_jwt_identity()

        # Retrieve the user from the database using the user ID
        user = User.objects(id=user_id).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Return user details (you can include additional fields here)
        user_data = {
            "username": user.username,
            "email": user.email,
            # Add more user fields as necessary
        }
        print(user_data)
        return jsonify(user_data), 200

    except Exception as e:
        print({"error": str(e)})
        return jsonify({"error": str(e)}), 500
