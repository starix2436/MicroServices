DATABASE = {
    "NAME": "auth_db",
    "USER": "starix",
    "PASSWORD": "starix",
    "HOST": "localhost",
    "PORT": "5432",
}

SQLALCHEMY_DATABASE_URI = (
    "postgresql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s" % DATABASE
)
SQLALCHEMY_TRACK_MODIFICATIONS = True
AUTH_GRPC_CHANNEL = "localhost:4001"
NOTIFICATION_GRPC_CHANNEL = "localhost:4002"
FLASK_ADMIN_SWATCH = "cerulean"
SECRET_KEY = "mysecretkey"
