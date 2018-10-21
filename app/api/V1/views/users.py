from flask import Flask, jsonify, request, make_response, Blueprint
import re
from flask_restful import Resource, reqparse
from app.api.V1.models import User, userList
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class UserRegistration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True, help='Email cannot be blank')
    parser.add_argument('password', required=True, help='Password cannot be blank', type=str)

    def post(self):

        args = UserRegistration.parser.parse_args()
        raw_password = args.get('password')
        confirm_password = args.get('confirm_password')
        username = args.get('username').strip()  # remove all whitespaces from input
        email = args.get('email').strip()  # remove all whitespaces from input

        # validate user input
        email_format = re.compile(
            r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")
        username_format = re.compile(r"(^[A-Za-z0-9-]+$)")

        if not email:
            return make_response(jsonify({'message': 'email can not be empty'}), 400)
        if not raw_password:
            return make_response(jsonify({'message': 'password cannot be empty'}), 400)
        if not username:
            return make_response(jsonify({'message': 'username cannot be empty'}), 400)
        if len(raw_password) < 6:
            return make_response(jsonify({'message': 'Password should be at least 6 characters'}), 400)
        if not (re.match(email_format, email)):
            return make_response(jsonify({'message': 'Invalid email'}), 400)
        if not (re.match(username_format, username)):
            return make_response(jsonify({'message': 'Please input only characters and numbers'}), 400)

         # check if user by the email exists
        current_user = User.find_by_email(email)
        if current_user == 1:
            return {
                'message': 'email already exist'
            }, 400

        # check if user by the email exists
        current_user = User.find_by_username(username)
        if current_user == 1:
            return {
                'message': 'username already exist'
            }, 400

        # generate hash for user password
        password = User.generate_hash(raw_password)

        # attempt sending user to user model
        try:
            result = User.create_user(username, email, password)
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            return {
                'message': 'User was created succesfully!',
                'status': 'ok',
                'password': password,
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 201

        except Exception as e:
            print(e)
            return {
                'message': 'Something went wrong'
            }, 500


class UserLogin(Resource):

    # validate user input
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='Email cannot be blank')
    parser.add_argument('password', required=True, help='Password cannot be blank')

    def post(self):
        data = request.get_json()
        # check for white spaces
        args = UserLogin.parser.parse_args()
        password = args.get('password').strip()  # remove whitespace
        email = args.get('email').strip()  # remove whitespace
        if not email:
            return {
                'message': 'email field can not be empty'
            }, 400
        if not password:
            return {
                'message': 'password field cannot be empty'
            }, 400

        # check if user by the email exists
        current_user = User.find_by_email(email)
        if current_user == 0:
            return {
                'message': 'email {} doesn\'t exist'.format(email)
            }, 400

        # compare user's password and the hashed password
        if User.verify_hash(password, email) == True:
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)

            return {
                'message': 'User logged in succesfully!',
                'status': 'ok',

                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        else:
            return {
                'message': 'Incorrect credentials'
            }, 400


class GetAllUsers(Resource):

    def get(self):
        return userList


class GetEachUser(Resource):

    @jwt_required
    def get(self, id):
        return userList[id - 1]
