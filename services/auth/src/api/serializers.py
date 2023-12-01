from marshmallow import Schema, fields


class SignSchema(Schema):
    username = fields.Integer(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
