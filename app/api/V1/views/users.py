from flask import request
from flask_restful import Resource
from app.api.V1.models import UserModel, userList
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class UserRegistration(Resource):

    def post(self):
        data = request.get_json()

        UserModel.create_user()

        try:
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
            return {'message': 'Something went wrong'}, 500
        # return {
        #     'message': 'User {} was created'.format(data['username'])
        # }, 201

    # @jwt_required
    # def get(self):
    #     return userList


class UserLogin(Resource):

    def post(self):
        data = request.get_json()

        for i in userList:
            if i['username'] == data['username']:
                if UserModel.verify_hash(data['password'], i['password']):
                    access_token = create_access_token(identity=data['username'])
                    refresh_token = create_refresh_token(identity=data['username'])
                return {
                    'message': 'Logged in as {}'.format(data['username']),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            else:
                return {'message': 'User doesn\'t exist'}

    # Get each user
    @jwt_required
    def get(self, id):
        try:
            result = User.get_each_user(id)
        except IndexError:
            return "The Id does not exist"
        return result


class GetAllUsers(Resource):

    @jwt_required
    def get(self):
        return userList


class GetEachUser(Resource):

    @jwt_required
    def get(self, id):
        return userList[id - 1]


# class TokenRefresh(Resource):
#     @jwt_refresh_token_required
#     def post(self):
#         current_user = get_jwt_identity()
#         access_token = create_access_token(identity=current_user)
#         return {'access_token': access_token}
