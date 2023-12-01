from marshmallow import Schema,fields

class SignSchema(Schema):
    username=fields.Integer(),
    email=fields.String(),
    password=fields.String(),
    first_name=fields.String(),
    last_name=fields.String(),

