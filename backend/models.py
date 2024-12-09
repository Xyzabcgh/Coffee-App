from flask_mongoengine import MongoEngine

# Initialize MongoEngine
db = MongoEngine()

# Define the User model
class User(db.Document):
    username = db.StringField(required=True, unique=True, max_length=50)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
