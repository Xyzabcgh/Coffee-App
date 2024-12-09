from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    # Set Mongo URI from environment variable or use default
    app.config["MONGO_URI"] = app.config.get("MONGO_URI", "mongodb://localhost:27017/coffee_delivery")
    mongo.init_app(app)
