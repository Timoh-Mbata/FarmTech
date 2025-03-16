from flask import Blueprint, request, jsonify
from ...apps.database import db
from ...apps.orders.models import Order
orders_bp = Blueprint("orders", __name__)
@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    try:
        new_order = Order(
            farmer_id=data['farmer_id'],
            buyer_id=data['buyer_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            total_price=data['total_price']
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"message": "Order created successfully", "order": new_order.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@orders_bp.route('/orders', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

# buyers to vue orders : 
@orders_bp.route('/orders/buyer/<int:buyer_id>', methods=['GET'])
def get_buyer_orders(buyer_id):
    orders = Order.query.filter_by(buyer_id=buyer_id).all()
    if not orders:
        return jsonify({"message": "No orders found for this buyer"}), 404
    return jsonify([order.to_dict() for order in orders]), 200
# farmers
@orders_bp.route('/orders/farmer/<int:farmer_id>', methods=['GET'])
def get_farmer_orders(farmer_id):
    orders = Order.query.filter_by(farmer_id=farmer_id).all()
    if not orders:
        return jsonify({"message": "No orders found for this farmer"}), 404
    return jsonify([order.to_dict() for order in orders]), 200

# get one order :
@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict()), 200

# update orders :
@orders_bp.route('/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()
    order.status = data.get('status', order.status)

    db.session.commit()
    return jsonify({"message": "Order status updated successfully", "order": order.to_dict()}), 200

# delete order :
@orders_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted successfully"}), 200

