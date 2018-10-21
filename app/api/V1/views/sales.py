from flask import Flask, jsonify, request, make_response, Blueprint

from flask_restful import Resource, reqparse
from app.api.V1.models import Sale
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

salesList = []


class PostSale(Resource):

     # Input validation

    parser = reqparse.RequestParser()
    parser.add_argument('description', required=True, help='Sale description  cannot be blank', type=str)
    parser.add_argument('items', required=True, help=' items cannot be blank')
    parser.add_argument('total', required=True, help='Total cannot be blank', type=int)

    @jwt_required
    def post(self):
        args = PostSale.parser.parse_args()
        description = args.get('description').strip()
        items = args.get('items')
        total = 400

        # Test inputs
        if not description:
            return make_response(jsonify({'message': 'Sale description  can not be empty'}), 400)
        if not items:
            return make_response(jsonify({'message': 'Sale items  can not be empty'}), 400)
        if not total:
            return make_response(jsonify({'message': 'Total cannot be empty'}), 400)

        try:

            sale = Sale.create_sale(description, items, total)

            return {
                'message': 'Sale record created successfully!',
                'sales': sale,
                'status': 'ok'

            }, 201

        except Exception as e:
            print(e)
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

        result = Sale.get_each_sale(sale_id)

        return {
            'message': 'Sale record retrieved succesfully!',
            'status': 'ok',
            'products': result
        }, 200
