from flask import request, Blueprint

from flask_restful import Resource
from app.api.V1.models import Sale

from flask_jwt_extended import jwt_required


salesList = []


class PostSale(Resource):

    @jwt_required
    def post(self):
        data = request.get_json()
        name = data['name']
        price = data['price']
        sale = Sale.create_sale_record(name, price)
        return {'message': 'Sale posted succesfully',
                'salerecord': sale,
                'status': 'ok'
                }, 201


class GetAllSales(Resource):

    @jwt_required
    def get(self):
        result = Sale.get_all_sales()
        return result


class GetEachSale(Resource):

    @jwt_required
    def get(self, id):
        result = Sale.get_each_sale(id)
        return result
