from flask_restx import Resource
from flask.views import MethodView
from app import swagger_api
from flask import request
from utils import *
from .swagger import (
    signup_model,
    login_model,
    user_id_request_params,
    filter_request_param,
    update_model,
)
from marshmallow import ValidationError
from api.serializers import SignSchema, UserSchema


class Hello(Resource, MethodView):
    @swagger_api.doc()
    def get(self):
        return {"hello": "rest x"}


class SignUp(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(signup_model)
    def post(self):
        data = request.get_json()
        try:
            data2 = SignSchema().load(data)
        except ValidationError as err:
            return err.messages
        new_acc = UserManager().signup(data2)
        return new_acc


class Login(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(login_model)
    def post(self):
        data = request.get_json()
        message = LoginManager().login(data)
        return message


class UserDetails(Resource, MethodView):
    @swagger_api.doc(params=user_id_request_params)
    def get(self):
        id = request.args.get("id")
        user = UserManager().details(id)
        data = UserSchema().dump(user)
        return data


class UserList(Resource, MethodView):
    @swagger_api.doc(params=filter_request_param)
    def get(self):
        user = UserManager(request).alldetails()
        data = UserSchema(many=True).dump(user)
        return data


class UpdateUser(Resource, MethodView):
    @swagger_api.doc(params=user_id_request_params)
    @swagger_api.expect(update_model)
    def put(self):
        id = request.args.get("id")
        data = request.get_json()
        user = UpdateManager().update(id, data)
        return user


class DeleteUser(Resource, MethodView):
    @swagger_api.doc(params=user_id_request_params)
    def delete(self):
        id = request.args.get("id")
        user = DeleteManager().delete(id)
        return user
