from flask_restx import Resource
from flask.views import MethodView
from app import swagger_api
from flask import request
from werkzeug.security import generate_password_hash
from models import User
from .serializers import signup_model, login_model


class Hello(Resource, MethodView):
    @swagger_api.doc()
    def get(self):
        return {"hello": "restx"}


class sign_up(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(signup_model)
    def post(self):
        data = request.get_json()

        if not data:
            return {"message": "No input data provided"}

        new_acc = User(
            username=data.get("username"),
            email=data.get("email"),
            password_hash=generate_password_hash(data.get("password")),
        )
        new_acc.save()
        return "success"


class Login(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(login_model)
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        user = User.query.filter_by(email=email).first()

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
