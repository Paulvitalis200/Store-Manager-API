from flask import request, Blueprint

from flask_restful import Resource
from app.api.V1.models import Sale


salesList = []


class PostSale(Resource):

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
    def get(self):
        result = Sale.get_all_sales()
        return result


class GetEachSale(Resource):
    pass
