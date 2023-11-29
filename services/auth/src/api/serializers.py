from flask_restx import fields
from app import swagger_api

signup_model = swagger_api.model(
    "User",
    {
        "username": fields.String(required=True, description="A username"),
        "first_name": fields.String(required=True, description="First name"),
        "last_name": fields.String(required=True, description="Last name"),
        "email": fields.String(required=True, description="An email"),
        "password": fields.String(required=True, description="A password"),
    },
)

login_model = swagger_api.model(
    "Login",
    {
        "email": fields.String(required=True, description="An email"),
        "password": fields.String(required=True, description="A password"),
    },
)
