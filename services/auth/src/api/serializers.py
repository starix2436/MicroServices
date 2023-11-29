
from flask_restx import fields
from app import swagger_api

signup_model = swagger_api.model("User", {
    'id': fields.Integer,
    'username':fields.String(required=True,description="A username"),
    'email':fields.String(required=True,description="An email"),
    'password':fields.String(required=True,description="A password"),
    'confirm_password':fields.String(required=True,description="confirm_password"),
})
   