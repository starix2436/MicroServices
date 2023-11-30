from flask_restx import Resource
from flask.views import MethodView
from app import swagger_api, db
from flask import request
from utils import signup, login

# from werkzeug.security import generate_password_hash
from models import User
from .serializers import signup_model, login_model


class Hello(Resource, MethodView):
    @swagger_api.doc()
    def get(self):
        return {"hello": "restx"}


class SignUp(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(signup_model)
    def post(self):
        data = request.get_json()
        message = signup(data)
        return message


class Login(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(login_model)
    def post(self):
        data = request.get_json()
        message = login(data)
        return message
