from flask_admin.contrib.sqla import ModelView
from app import  db,admin

# from flask_admin import Admin


# admin = Admin(app, name="Auth", template_mode="bootstrap3", url=f"{url_prefix}/admin")
from models import User, PhoneNumber

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(PhoneNumber, db.session))
