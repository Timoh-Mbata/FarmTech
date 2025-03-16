from flask import render_template
from . import farmers_bp
@farmers_bp.route("/dashboard")
def dashboard():
    """Render Farmer Dashboard."""
    return render_template("farmers/dashboard.vue")
