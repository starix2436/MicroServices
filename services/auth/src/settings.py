import os
from datetime import datetime, timedelta

DATABASE = {
    "NAME": os.environ.get("AUTH_DATABASE_NAME"),
    "USER": os.environ.get("AUTH_DATABASE_USER"),
    "PASSWORD": os.environ.get("AUTH_DATABASE_PASSWORD"),
    "HOST": os.environ.get("AUTH_DATABASE_HOST"),
    "PORT": os.environ.get("AUTH_DATABASE_PORT"),
}
