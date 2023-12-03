from flask_restx import Resource
from flask.views import MethodView
from app import swagger_api, db
from flask import request, jsonify
from utils import UserManager, LoginManager, UpdateManager


# from serializers import UserSchema

# from werkzeug.security import generate_password_hash
from models import User
from .swagger import (
    signup_model,
    login_model,
    contract_consumer_list_request_params,
    update_model
)

from marshmallow import ValidationError, post_load
from api.serializers import SignSchema, UserSchema


class Hello(Resource, MethodView):
    @swagger_api.doc()
    def get(self):
        return {"hello": "restx"}


class SignUp(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(signup_model)
    def post(self):
        data = request.get_json()
        # schema = SignSchema()
        # person = schema.dump(data)
        try:
            data2 = SignSchema().load(data)
        except ValidationError as err:
            # logger.error(f"{err.messages}")
            return err.messages
        print(data2, "----------------")
        new_acc = UserManager().signup(data2)
        # result=schema.load(new_acc)
        return new_acc


class Login(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(login_model)
    def post(self):
        data = request.get_json()
        message = LoginManager().login(data)
        return message


class UserDetails(Resource, MethodView):
    @swagger_api.doc(params=contract_consumer_list_request_params)
    def get(self):
        id = request.args.get("id")
        user = UserManager().details(id)
        #print(user, "---------------")
        data = UserSchema().dump(user)
        #print(data, "---------------")
        return data

class UserList(Resource,MethodView):
    @swagger_api.doc()
    def get(self):
        user = UserManager().alldetails()
        data = UserSchema(many=True).dump(user)
        return data

class UpdateUser(Resource,MethodView):
    @swagger_api.doc(params=contract_consumer_list_request_params)
    @swagger_api.expect(update_model)
    def put(self):
        id = request.args.get("id")
        data = request.get_json()
        user = UpdateManager().update(id,data)
        return user




