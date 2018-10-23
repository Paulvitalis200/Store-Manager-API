from flask import Flask, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required

from app.api.V1.models import Product, products


class PostProduct(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help='Product name cannot be blank', type=str)
    parser.add_argument('price', required=True, help=' Product price cannot be blank or a word', type=int)
    parser.add_argument('quantity', required=True, help='Product quantity cannot be blank or a word', type=int)

    @jwt_required
    def post(self):
        # input validation
        data = request.get_json()
        args = PostProduct.parser.parse_args()
        name = args.get('name').strip()  # removes whitespace
        price = args.get('price')
        quantity = args.get('quantity')
        payload = ['name', 'price', 'quantity']

        if not name:
            return {'message': 'Product name cannot be empty'}, 400
        elif not price:
            return {'message': 'Price of product cannot be empty'}, 400
        elif not quantity:
            return {'message': 'Quantity of product cannot be empty'}, 400
        else:
            # Check if the item is not required
            for item in data.keys():
                if item not in payload:
                    return {"message": "The field '{}' is not required for the products".format(item)}, 400

        try:
            product = Product.create_product(name, price, quantity)
            return {
                'message': 'Product created successfully!',
                'product': product,
                'status': 'ok'
            }, 201

        except Exception as my_exception:
            print(my_exception)
            return {'message': 'Something went wrong.'}, 500


class GetAllProducts(Resource):
    # Both attendant and store owner can get products
    @jwt_required
    def get(self):
        products = Product.get_products()
        return {
            'message': 'Products successfully retrieved!',
            'products': products
        }, 200


# Get a single specific product
class GetEachProduct(Resource):
    @jwt_required
    def get(self, product_id):
        try:
            return products[product_id - 1]
        except IndexError:
            return {"message": "No item with that ID in stock"}
