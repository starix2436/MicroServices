from flask_restx import Resource
from flask.views import MethodView
from app import swagger_api, db
from flask import request,jsonify
from utils import UserManager, LoginManager
from api.serializers import SignSchema

# from werkzeug.security import generate_password_hash
from models import User
from .swagger import signup_model, login_model
from marshmallow import post_load

class Hello(Resource, MethodView):
    @swagger_api.doc()
    def get(self):
        return {"hello": "restx"}


class SignUp(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(signup_model)
    def post(self):
        data = request.get_json()
        new_acc = UserManager().signup(data)
        # serializer=SignSchema()
        # result=serializer.load(new_acc)
        # person=serializer.dump(result)
        return new_acc


class Login(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(login_model)
    def post(self):
        data = request.get_json()
        message = LoginManager().login(data)
        return message
