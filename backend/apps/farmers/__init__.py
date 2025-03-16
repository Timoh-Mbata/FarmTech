from flask import Blueprint
from ...apps.farmers.routes import farmers_bp
def register_farmers(app):
    app.register_blueprint(farmers_bp)

