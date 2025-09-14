from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from socketio_instance import socketio
from models import db
from routes.auth import auth_bp
from routes.donations import donations_bp
import os
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

app = Flask(__name__)

# -----------------------------
# CORS setup
# -----------------------------
cors_origins = os.getenv("CORS_ORIGIN")
CORS(app, origins=cors_origins, supports_credentials=True, methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

# -----------------------------
# Configs
# -----------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")  # Supabase Postgres URL from environment variable
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "your-secret-key")

# Set JWT access token expiration to 1 day
from datetime import timedelta
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

# -----------------------------
# Initialize extensions
# -----------------------------
db.init_app(app)
jwt = JWTManager(app)
socketio.init_app(app, cors_allowed_origins="*")

# -----------------------------
# Blueprints / Routes
# -----------------------------
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(donations_bp, url_prefix="/donations")

# -----------------------------
# Health check route
# -----------------------------
@app.route("/")
def home():
    return jsonify({"message": "HungerFree API running!"})

# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # create tables if they don't exist
    socketio.run(app, debug=True)
