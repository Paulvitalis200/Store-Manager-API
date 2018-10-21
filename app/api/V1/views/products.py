from flask import request

from flask_restful import Resource
from app.api.V1.models import Product

from flask_jwt_extended import jwt_required


class PostProduct(Resource):

    @jwt_required
    def post(self):
        data = request.get_json()
        p = ['name', 'price']
        for i in data.keys():
            if i not in p:
                return {"message": "The field {} is not needed".format(i)}, 400
                # test
        if 'name' not in data:
            return {"msg": "please provide name"}, 400
            # test

        name = data['name']

        price = data['price']
        # edge case and test

        result = Product.create_product(name, price)
        return {'message': 'product created succesfully',
                'products': result,
                'status': 'ok'
                }, 201


class GetAllProducts(Resource):
    # Both attendant and store owner can get products
    @jwt_required
    def get(self):
        result = Product.get_all_products()
        return result


class GetEachProduct(Resource):

    # Both attendant and store owner can get an individual product
    @jwt_required
    def get(self, id):
        try:
            result = Product.get_each_product(id)
        except IndexError:
            return "The Id does not exist"
        return result
