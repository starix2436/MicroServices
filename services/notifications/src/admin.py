<<<<<<< Updated upstream
=======
from flask_admin.contrib.sqla import ModelView
from app import app, db
from flask_admin import Admin
from models import BaseModel


url_prefix = "/notifications"

admin = Admin(app, name="notifications", template_mode="bootstrap3", url=f"{url_prefix}/admin")

admin.add_view(ModelView(BaseModel, db.session))
>>>>>>> Stashed changes
