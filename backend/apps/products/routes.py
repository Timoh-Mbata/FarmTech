import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from .models import Product
from ...apps.database import db
from flask_cors import CORS

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi'}

products_bp = Blueprint('products', __name__)
CORS(products_bp)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@products_bp.route('/farmers/<int:farmer_id>/products', methods=['GET'])
def get_products(farmer_id):
    products = Product.query.filter_by(farmer_id=farmer_id).all()
    return jsonify([product.to_dict() for product in products])

@products_bp.route('/farmers/<int:farmer_id>/products', methods=['POST'])
def add_product(farmer_id):
    data = request.form
    file = request.files.get('file')

    file_url = None
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        file_url = f"/static/uploads/{filename}"

    new_product = Product(
        name=data['name'],
        price=float(data['price']),  # Ensure price is float
        description=data.get('description', ''),
        farmer_id=farmer_id,
        media_url=file_url  # Store file URL in DB
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added successfully!", "file_url": file_url}), 201

@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        if product.media_url:
            file_path = product.media_url.lstrip("/")
            if os.path.exists(file_path):
                os.remove(file_path)

        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully!"}), 200

    return jsonify({"error": "Product not found"}), 404

@products_bp.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    print(products)
    return jsonify([product.to_dict() for product in products])
