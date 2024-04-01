from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Product
from app import db

bp = Blueprint('product_routes', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def list_products():
    products = Product.query.all()
    product_data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
    return jsonify(product_data), 200

@bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    product_data = {'id': product.id, 'name': product.name, 'price': product.price}
    return jsonify(product_data), 200

@bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    if not name or not price:
        return jsonify({'message': 'Name and price are required'}), 400

    product = Product(name=name, price=price)
    db.session.add(product)
    db.session.commit()

    return jsonify({'message': 'Product created successfully'}), 201

@bp.route('/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')

    if name:
        product.name = name
    if price:
        product.price = price

    db.session.commit()

    return jsonify({'message': 'Product updated successfully'}), 200

@bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully'}), 200
