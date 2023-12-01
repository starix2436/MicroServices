from marshmallow import Schema, fields
from models import User
from app import ma


class SignSchema(Schema):
    username = fields.Integer(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
