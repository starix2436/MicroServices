from flask_restx import fields
from app import swagger_api

user_id_request_params = {
    "id": {"description": "Enter user id", "type": "int", "default": None}
}

filter_request_param = {
    "first name": {
        "description": "Enter user first name to filter",
        "type": "str",
        "default": None,
    },
    "last name": {
        "description": "Enter user last name to filter",
        "type": "str",
        "default": None,
    },
    "username": {
        "description": "Enter user username to filter",
        "type": "str",
        "default": None,
    },
    "email": {
        "description": "Enter user email to filter",
        "type": "str",
        "default": None,
    },
}

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

update_model = swagger_api.model(
    "User",
    {
        "username": fields.String(required=True, description="A username"),
        "first_name": fields.String(required=True, description="First name"),
        "last_name": fields.String(required=True, description="Last name"),
        "email": fields.String(required=True, description="An email"),
        "password": fields.String(required=True, description="A password"),
    },
)
