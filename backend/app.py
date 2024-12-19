from flask import Flask
from flask_cors import CORS
from routes.auth import auth_blueprint

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for API calls

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
