from flask_restx import Resource
from flask.views import MethodView
from app import swagger_api, db, bcrypt
from flask import request

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

        if not data:
            return {"message": "No input data provided"}

        hashed_password = bcrypt.generate_password_hash(data.get("password")).decode(
            "utf-8"
        )
        new_acc = User(
            username=data.get("username"),
            email=data.get("email"),
            password=hashed_password,
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
        )
        db.session.add(new_acc)
        db.session.commit()
        return "success"


class Login(Resource, MethodView):
    @swagger_api.doc()
    @swagger_api.expect(login_model)
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        user = User.get_user(email=email).first()
        print(user)
        if user and bcrypt.check_password_hash(user.password, password):
            return {
                "message": "Login successful",
                "user_id": user.id,
                "username": user.username,
            }
        else:
            return {
                "message": "Login unsuccessful",
            }
