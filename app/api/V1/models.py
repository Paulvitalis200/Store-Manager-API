from flask import jsonify, request, Blueprint
from passlib.hash import pbkdf2_sha256 as sha256
from flask_restful import Resource, Api


cart = []
salesList = []
userList = []

# Fixed Bug


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


class UserModel():
        # create user
    def create_user():
        data = request.get_json()
        id = len(userList) + 1
        username = data['username']
        password = UserModel.generate_hash(data['password'])
        user = {
            'username': username,
            'password': password
        }
        userList.append(user)
        return user

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    # get all product store owner and store attendant
    # def get_all_users():
    #     return userList

    # # store owner and store attendant get each product
    # def get_each_user(id):
    #     return userList[id - 1]
