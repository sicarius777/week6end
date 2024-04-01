from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Product, Cart
from app import db

bp = Blueprint('cart_routes', __name__, url_prefix='/cart')

@bp.route('/', methods=['GET'])
@jwt_required()
def view_cart():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    cart_items = user.cart_items
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    cart_data = [{'product': item.product.name, 'quantity': item.quantity} for item in cart_items]
    return jsonify({'cart': cart_data, 'total_price': total_price}), 200

@bp.route('/add', methods=['POST'])
@jwt_required()
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    if not product_id:
        return jsonify({'message': 'Product ID is required'}), 400

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    existing_item = Cart.query.filter_by(user_id=current_user_id, product_id=product_id).first()

    if existing_item:
        existing_item.quantity += quantity
    else:
        cart_item = Cart(user_id=current_user_id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()

    return jsonify({'message': 'Product added to cart successfully'}), 201

@bp.route('/remove/<int:product_id>', methods=['DELETE'])
@jwt_required()
def remove_from_cart(product_id):
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    cart_item = Cart.query.filter_by(user_id=current_user_id, product_id=product_id).first()

    if not cart_item:
        return jsonify({'message': 'Product not found in cart'}), 404

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({'message': 'Product removed from cart successfully'}), 200

@bp.route('/clear', methods=['DELETE'])
@jwt_required()
def clear_cart():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    cart_items = Cart.query.filter_by(user_id=current_user_id).all()

    for item in cart_items:
        db.session.delete(item)
    db.session.commit()

    return jsonify({'message': 'Cart cleared successfully'}), 200
