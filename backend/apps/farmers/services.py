from ...apps.database import db
from .models import Farmer
def create_farmer(data):
    """Registers a new farmer."""
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    location = data.get('location')
    password = data.get("password")

    if Farmer.query.filter_by(email=email).first():
        return {"message": "Email already exists"}, 400
    new_farmer = Farmer(username=name, phone=phone,location = location, email=email)
    new_farmer.set_password(password)
    db.session.add(new_farmer)
    db.session.commit()
    return {"message": "Farmer registered successfully"}, 201

def authenticate_farmer(data):
    """Handles farmer login."""
    email = data.get("email")
    password = data.get("password")
    farmer = Farmer.query.filter_by(email=email).first()
    if not farmer or not farmer.check_password(password):
        return {"message": "Invalid credentials"}, 401

    return {"message": "Login successful"}, 200
