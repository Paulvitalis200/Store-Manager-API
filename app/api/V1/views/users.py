import re
import datetime

from flask import Flask, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required

from app.api.V1.models import User, userList


class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True, help='Email cannot be blank')
    parser.add_argument('password', required=True, help='Password cannot be blank', type=str)

    def post(self):
        data = request.get_json()
        args = UserRegistration.parser.parse_args()
        raw_password = args.get('password').strip()
        username = args.get('username').strip()  # remove all whitespaces from input
        email = args.get('email').strip()  # remove all whitespaces from input
        payload = ['username', 'password', 'email']

        # User input validations
        email_format = re.compile(r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")
        username_format = re.compile(r"(^[A-Za-z0-9-]+$)")

        if not email:
            return {'message': 'Email cannot be empty'}, 400
        elif not raw_password:
            return {'message': 'Password cannot be empty'}, 400
        elif not username:
            return {'message': 'Username cannot be empty'}, 400
        elif len(raw_password) < 6:
            return {'message': 'Password should be at least 6 characters'}, 400
        elif not (re.match(email_format, email)):
            return {'message': 'Invalid email'}, 400
        elif not (re.match(username_format, username)):
            return {'message': 'Please input only characters and numbers'}, 400
        else:
            # Check if the item is not required
            for item in data.keys():
                if item not in payload:
                    return {"message": "The field '{}' is not required for registration".format(item)}, 400

        # Check if user by the email exists
        current_user = User.find_by_username(username)
        if current_user != False:
            return {
                'message': 'A user with that username already exists.'
            }, 400

        # Check if user by the email exists
        current_user = User.find_by_email(email)
        if current_user != False:
            return {
                "message": "A user with that email already exists."
            }, 400

        # Generate hash for user password
        password = User.generate_hash(raw_password)

        # Try to send the registered user to the user model
        try:
            result = User.create_user(username, email, password)
            return {
                'message': '{} was registered succesfully!'.format(username),
                'status': 'ok',
                'password': password
            }, 201

        except Exception as my_exception:
            print(my_exception)
            return {
                'message': 'Something went wrong'
            }, 500


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='Email cannot be blank')
    parser.add_argument('password', required=True, help='Password cannot be blank')

    def post(self):
        data = request.get_json()
        args = UserLogin.parser.parse_args()
        password = args.get('password').strip()  # remove whitespace
        email = args.get('email').strip()  # remove whitespace
        payload = ['password', 'email']
        if not email:
            return {
                'message': 'email field cannot be empty'
            }, 400
        elif not password:
            return {
                'message': 'password field cannot be empty'
            }, 400
        else:
            for item in data.keys():
                if item not in payload:
                    return {"message": "The field '{}' is not required for login".format(item)}, 400

        # check if user by the email exists
        current_user = User.find_by_email(email)
        if current_user == False:
            return {
                'message': 'User with that email does not exist.'
            }, 400

        # compare user's password and the hashed password
        if User.verify_hash(password, email) == True:
            access_token = create_access_token(identity=email, expires_delta=datetime.timedelta(days=5))
            return {
                'message': 'Log in successful!',
                'status': 'ok',
                'access_token': access_token,
            }, 200
        else:
            return {
                'message': 'Incorrect email or password. Try again'
            }, 400


class GetAllUsers(Resource):

    @jwt_required
    def get(self):
        return userList


class GetEachUser(Resource):

    @jwt_required
    def get(self, id):
        try:
            return userList[id - 1]
        except IndexError:
            return {"message": "No user with that id available"}
