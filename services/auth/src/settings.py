import os
from datetime import datetime, timedelta

DATABASE = {
    "NAME": ,
    "USER": ,
    "PASSWORD":, 
    "HOST": ,
    "PORT": 
}

SQLALCHEMY_DATABASE_URI = "postgresql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s" % DATABASE
SQLALCHEMY_TRACK_MODIFICATIONS = False 
AUTH_GRPC_CHANNEL = "localhost:401"
NOTIFICATION_GRPC_CHANNEL = "localhost:402"