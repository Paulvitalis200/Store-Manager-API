from flask import jsonify, request, Blueprint, make_response

from flask_restful import Resource, Api, reqparse
from passlib.hash import pbkdf2_sha256 as sha256


products = []
cart = []
userList = [
    {
        "username": "Paul",
        "email": "vitalispaul48@live.com",
        "password": "$pbkdf2-sha256$29000$PKd0DmGM8f4fAwCAUKq1Ng$Ze0Lb9BnUbsbldDMfPXJ8Cjcc7TK5LcjZUXqx8pCt/Y"
    }
]


class User():

    @staticmethod
    def create_user(username, email, password):
        role = 'user'
        id = len(userList) + 1
        new_user = {
            'id': id,
            'username': username,
            'email': email,
            'password': password,
            'role': role
        }
        userList.append(new_user)
        return userList

    # find if email exists
    @staticmethod
    def find_by_email(email):
        for user in userList:
            listOfKeys = [key for (key, value) in user.items() if value == email]
            if listOfKeys:
                return 1
            return 0

    # find if username exists
    @staticmethod
    def find_by_username(username):
        for user in userList:
            listOfKeys = [key for (key, value) in user.items() if value == username]
            if listOfKeys:
                return 1
            return 0

     # generate hash
    @staticmethod
    def generate_hash(raw_password):
        return sha256.hash(raw_password)

    # compare user password with hashed password
    @staticmethod
    def verify_hash(password, email):
        for user in userList:
            listOfKeys = [key for (key, value) in user.items() if value == email]
            if listOfKeys:
                result = list(filter(lambda person: person['email'] == email, userList))
                return sha256.verify(password, result[0]['password'])


class Product():

    # create a new product - admin
    @staticmethod
    def create_product(name, price, quantity):
        id = len(products) + 1
        new_product = {
            'id': id,
            'name': name,
            'price': price,
            'quantity': quantity
        }
        products.append(new_product)
        return products

# Get all products
    @staticmethod
    def get_products():
        return products


# Get a single product
    @staticmethod
    def get_each_product(product_id):
        product_index = product_id - 1
        return products[product_index]


class Sale():

    # create a sale record- store attendant
    @staticmethod
    def create_sale(description, items, total):
        id = len(cart) + 1
        order = {
            'id': id,
            'description': description,
            'items': items,
            'total': total
        }
        cart.append(order)
        return cart


# Get all sales
    @staticmethod
    def get_all_sales():
        return cart


# fetch a single sale
    @staticmethod
    def get_each_sale(sale_id):
        sale_index = sale_id - 1
        return cart[sale_index]
