from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restx import Api, Namespace, apidoc

app = Flask(__name__)
app.config.from_pyfile("settings.py")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
url_prefix = "/auth"
from admin import *

swagger_desc = ""

apidoc.apidoc.url_prefix = url_prefix
swagger_api = Api(
    app,
    version="v1.0",
    title="RELYbill",
    description=swagger_desc,
    doc=f"{url_prefix}/swagger/",
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    prefix=url_prefix,
)
# api = Api(app, version="v1.0", doc=f"{url_prefix}/swagger/", prefix=url_prefix)
from api.api_urls import *

if __name__ == "__main__":
    app.run(debug=True)
