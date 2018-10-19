from flask import request

from flask_restful import Resource
from app.api.V1.models import Product


class PostProduct(Resource):

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
