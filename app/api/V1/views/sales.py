from flask import Flask, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required

from app.api.V1.models import Sale, cart


class PostSale(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('description', required=True, help='Sale description cannot be blank or integer', type=str)
    parser.add_argument('items', required=True, help='Items cannot be blank', type=str)
    # parser.add_argument('total', required=True, help=' Sales total cannot be blank or a word', type=int)

    @jwt_required
    def post(self):
        data = request.get_json()
        args = PostSale.parser.parse_args()
        description = args.get('description').strip()
        items = args.get('items')
        payload = ['description', 'items']

        # Test inputs
        if not description:
            return {'message': 'Sale description cannot be empty'}, 400
        elif not items:
            return {'message': 'Sale items cannot be empty'}, 400
        else:
            # Check if the item is not required
            for each in data.keys():
                if each not in payload:
                    return {"message": "The field '{}' is not required for sales".format(each)}, 400

        try:
            sale = Sale.create_sale(description, items)
            return {
                'message': 'Sale record created successfully!',
                'sales': sale,
                'status': 'ok'
            }, 201
        except Exception as my_exception:
            print(my_exception)
            return {'message': 'Something went wrong'}, 500


class GetAllSales(Resource):
    @jwt_required
    def get(self):
        result = Sale.get_all_sales()
        return {
            'message': 'Sales records retrieved successfully!',
            'status': 'ok',
            'sale': result
        }, 200


class GetEachSale(Resource):
    @jwt_required
    def get(self, sale_id):
        try:
            return cart[sale_id - 1]
        except IndexError:
            return {"message": "No sale record with that ID in sales records"}
