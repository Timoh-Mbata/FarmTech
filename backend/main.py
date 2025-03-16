from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .apps.database import db
from flask_bcrypt import Bcrypt
from .apps.farmers import register_farmers
from .apps.products.routes import products_bp
from .apps.orders.routes import orders_bp
from .apps.configure.conf import Config
app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
db.init_app(app)
migrate = Migrate(app, db)
register_farmers(app)
app.register_blueprint(products_bp)
app.register_blueprint(orders_bp)
if __name__ == '__main__':
    app.run(debug=True)
