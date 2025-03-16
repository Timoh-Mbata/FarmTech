from flask import Blueprint, request, jsonify
from ...apps.database import db  # Adjust according to your app structure
from .models import Farmer  # Your Farmer model
from flask_bcrypt import Bcrypt
import datetime
import jwt

bcrypt = Bcrypt()
SECRET_KEY = 'your_secret_key'  # Replace with your actual secret key

farmers_bp = Blueprint("farmers", __name__)
@farmers_bp.route("/farmers/register", methods=["POST"])
def register_farmer():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400
        
        # Normalize and trim input
        name = data.get("name", "").strip()
        email = data.get("email", "").strip().lower()
        phone = data.get("phone", "").strip()
        location = data.get("location", "").strip()
        password = data.get("password", "").strip()

        if not all([name, email, phone, location, password]):
            return jsonify({"error": "Missing required fields"}), 400

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new Farmer instance
        new_farmer = Farmer(name=name, email=email, phone=phone, location=location, password=hashed_password)
        db.session.add(new_farmer)
        db.session.commit()

        return jsonify({"message": "Farmer registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@farmers_bp.route("/farmers/login", methods=["POST"])
def login_farmer():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request format"}), 400

        # Normalize inputs
        email = data.get("email", "").strip().lower()
        password = data.get("password", "").strip()

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        farmer = Farmer.query.filter_by(email=email).first()
        if not farmer or not bcrypt.check_password_hash(farmer.password, password):
            return jsonify({"error": "Invalid credentials"}), 401

        # Generate JWT token with Farmer ID and expiration
        token = jwt.encode(
            {
                "id": farmer.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=5)
            },
            SECRET_KEY,
            algorithm="HS256"
        )

        return jsonify({"message": "Login successful!", "token": token}), 200
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

# JWT token middleware
from functools import wraps
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is missing"}), 401
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return f(decoded, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
    return decorated

@farmers_bp.route("/farmers/<int:farmerId>", methods=["GET"])
@token_required
def get_farmer_by_id(decoded_token, farmerId):
    try:
        # Ensure the farmer can only access their own data
        if decoded_token.get("id") != farmerId:
            return jsonify({"error": "Unauthorized access"}), 403
        farmer = Farmer.query.get(farmerId)
        if not farmer:
            return jsonify({"error": "Farmer not found"}), 404
        return jsonify({
            "id": farmer.id,
            "name": farmer.name,
            "email": farmer.email,
            "phone": farmer.phone,
            "location": farmer.location
        }), 200
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500
