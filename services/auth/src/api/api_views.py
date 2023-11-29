from flask_restx import Resource
from flask.views import MethodView
from app import swagger_api


class Hello(Resource, MethodView):
    @swagger_api.doc()
    def get(self):
        return {"hello": "restx"}
