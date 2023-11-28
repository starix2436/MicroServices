from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os 


app= Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SECRET_KEY']='qwerty'
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)
# from .models import User
Migrate(app, db)
bcrypt = Bcrypt(app)
