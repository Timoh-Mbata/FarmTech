from ...apps.database import db
from flask_bcrypt import generate_password_hash, check_password_hash
class Farmer(db.Model):
    __tablename__ = "farmers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120),unique=True,nullable=False)
    location = db.Column(db.String(120),unique=False,nullable=False)
    password = db.Column(db.String(255), nullable=False)
    def set_password(self, password):
        self.password = generate_password_hash(password).decode("utf-8")
    def check_password(self, password):
        return check_password_hash(self.password, password)
