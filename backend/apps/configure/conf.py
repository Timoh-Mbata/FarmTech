import os
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:newpassword@localhost:5432/agrovet"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my_secret_key"

