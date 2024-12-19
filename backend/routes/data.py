from flask import Blueprint, request, jsonify
from firebase_config import db

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/add-data', methods=['POST'])
def add_data():
    data = request.json
    try:
        db.child("data").push(data)
        return jsonify({"message": "Data added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
