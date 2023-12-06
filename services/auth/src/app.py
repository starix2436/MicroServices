from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restx import Api, apidoc


app = Flask(__name__)
app.config.from_pyfile("settings.py")
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
url_prefix = "/auth"


from flask_admin import Admin


admin = Admin(app, name="Auth", template_mode="bootstrap3", url=f"{url_prefix}/admin")

swagger_desc = ""

apidoc.apidoc.url_prefix = url_prefix

swagger_api = Api(
    app,
    version="v1.0",
    title="MicroService",
    description=swagger_desc,
    doc=f"{url_prefix}/swagger/",
    authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    prefix=url_prefix,
)

from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

from api.api_urls import *

if __name__ == "__main__":
    app.run(debug=True)
