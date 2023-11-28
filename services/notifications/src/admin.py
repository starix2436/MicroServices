from flask_admin.contrib.sqla import ModelView
from app import app as  db
from flask_admin import Admin
from models import AuthToken, OTPDevice
 
 
admin = Admin( name='notifications', template_mode='bootstrap3')
 
admin.add_view(ModelView(AuthToken, db.session))
admin.add_view(ModelView(OTPDevice, db.session))