from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
import os
from routes.auth_routes import auth_bp

# Create the Flask app
app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGODB_SETTINGS'] = {
    'db': 'coffee_delivary_app',
    'host': os.getenv('MONGO_URI', 'mongodb://localhost:27017/coffee_delivary_app')
}

# Randomly generate JWT_SECRET_KEY (you can replace this with a more secure method)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-random-jwt-secret-key')

# Initialize MongoEngine and JWTManager
db = MongoEngine(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)
