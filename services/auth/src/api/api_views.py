from flask_restx import Resource
from flask.views import MethodView
from app import swagger_api, db
from flask import request
from utils import signup
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
        m=signup(data)
        return m



        # if not data:
        #     return {"message": "No input data provided"}

        # new_acc = User(
        #     username=data.get("username"),
        #     email=data.get("email"),
        #     password=data.get("password"),
        #     first_name=data.get("first_name"),
        #     last_name=data.get("last_name"),
        # )
        # db.session.add(new_acc)
        # db.session.commit()
        # return "success"


class Login(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(login_model)
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        user = User.get_user(email=email).first()

        if user and password == user.password:
            return {
                "message": "Login successful",
                "user_id": user.id,
                "username": user.username,
            }
        else:
            return {
                "message": "Login unsuccessful",
            }
