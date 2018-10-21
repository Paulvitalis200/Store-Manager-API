from flask import Flask, jsonify, request, make_response, Blueprint

from flask_restful import Resource, reqparse
from app.api.V1.models import Product, products
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class PostProduct(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help='Product name cannot be blank', type=str)
    parser.add_argument('price', required=True, help=' Product price cannot be blank', type=int)
    parser.add_argument('quantity', required=True, help='Product quantity cannot be blank', type=int)

    @jwt_required
    def post(self):
        # input validation
        args = PostProduct.parser.parse_args()
        name = args.get('name').strip()  # removes whitespace
        price = args.get('price')
        quantity = args.get('quantity')

        if not name:
            return make_response(jsonify({'message': 'Product name cannot be empty'}), 400)
        if not price:
            return make_response(jsonify({'message': 'Price of product cannot be empty'}), 400)
        if not quantity:
            return make_response(jsonify({'message': 'Quantity of product cannot be empty'}), 400)

        try:
            product = Product.create_product(name, price, quantity)
            return {
                'message': 'Product created successfully!', 'product': product, 'status': 'ok'
            }, 201

        except Exception as e:
            print(e)
            return {'message': 'Something went wrong.'}, 500


class GetAllProducts(Resource):
    # Both attendant and store owner can get products
    @jwt_required
    def get(self):
        products = Product.get_products()
        return {
            'message': 'Products successfully retrieved!',
            'status': 'ok',
            'products': products
        }, 200


# Get a single specific product
class GetEachProduct(Resource):
    @staticmethod
    def get(product_id):
        product_index = product_id - 1
        return products[product_index]
