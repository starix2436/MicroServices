import os
from datetime import datetime, timedelta

DATABASE = {
    "NAME": 'notifications',
    "USER": 'trellis',
    "PASSWORD":'admin123', 
    "HOST": 'localhost',
    "PORT": 5432
}



SQLALCHEMY_DATABASE_URI = 'postgresql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s' % DATABASE
#SQLALCHEMY_DATABASE_URI = 'postgresql://trellis:admin123@localhost:5432/notifications'
SQLALCHEMY_TRACK_MODIFICATIONS = True
AUTH_GRPC_CHANNEL = "localhost:4001"
NOTIFICATION_GRPC_CHANNEL = "localhost:4002"
FLASK_ADMIN_SWATCH='cerulean'
