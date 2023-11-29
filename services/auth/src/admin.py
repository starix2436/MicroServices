from flask_admin.contrib.sqla import ModelView
from app import app, db, url_prefix
from flask_admin import Admin



admin = Admin(app, name="Auth", template_mode="bootstrap3", url=f"{url_prefix}/admin")
from models import User
admin.add_view(ModelView(User, db.session))
