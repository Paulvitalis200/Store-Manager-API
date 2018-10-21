from flask import jsonify, request, Blueprint

from flask_restful import Resource, Api


cart = []
salesList = []


class Sale():
    # post product by admin
    def create_sale_record(name, price):
        id = len(salesList) + 1
        sale = {"id": id, "price": price, "name": name}
        salesList.append(sale)
        return salesList

# get all product
    def get_all_sales():
        return salesList

# get each product
    def get_each_sale(id):
        return salesList[id - 1]


class Product():
    # post product by admin
    def create_product(name, price):
        id = len(cart) + 1
        product = {"id": id, "price": price, "name": name}
        cart.append(product)
        return cart

    # get all product store owner and store attendant
    def get_all_products():
        return cart

    # store owner and store attendant get each product
    def get_each_product(id):
        return cart[id - 1]
