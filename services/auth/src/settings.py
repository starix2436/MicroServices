import os
from datetime import datetime, timedelta

DATABASE = {
    "NAME": os.environ.get("AUTH_DATABASE_NAME"),
    "USER": os.environ.get("AUTH_DATABASE_USER"),
    "PASSWORD": os.environ.get("AUTH_DATABASE_PASSWORD"),
    "HOST": os.environ.get("AUTH_DATABASE_HOST"),
    "PORT": os.environ.get("AUTH_DATABASE_PORT"),
}

SQLALCHEMY_DATABASE_URI = (
    "postgresql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s" % DATABASE
)
SQLALCHEMY_TRACK_MODIFICATIONS = bool(
    decode_base64(os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS"))
)
