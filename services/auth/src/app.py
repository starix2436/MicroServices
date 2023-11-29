from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restx import Api

app = Flask(__name__)
app.config.from_pyfile("settings.py")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
url_prefix = "/auth"
from admin import *

api = Api(app)
from api.api_views import ns

api.add_namespace(ns)

if __name__ == "__main__":
    app.run(debug=True)
