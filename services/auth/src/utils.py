# from flask import jsonify
from app import db, bcrypt
from models import User
from loggers import logger


class UserManager:
    def details(self, id):
        user = User.get_user_details(id)
        # show phone numbers also
        return user
    def alldetails(self):
        user=User.get_all()
        return user

    def signup(self, data):
        if not data:
            return {"message": "No input data provided"}
        email = data.get("email")
        user = User.get_user(email=email).first()

        try:
            if user == None:
                hashed_password = bcrypt.generate_password_hash(
                    data.get("password")
                ).decode("utf-8")
                new_acc = User(
                    username=data.get("username"),
                    email=data.get("email"),
                    password=hashed_password,
                    first_name=data.get("first_name"),
                    last_name=data.get("last_name"),
                )
                db.session.add(new_acc)
                db.session.commit()

                return {"message": "success"}
            else:
                return {"message": "enter different email"}
        except Exception as e:
            logger.error("some error occured", exc_info=e)
            return {"message": "an error occured "}


class LoginManager:
    def login(self, data):
        email = data.get("email")
        password = data.get("password")
        try:
            user = User.get_user(email=email).first()
            print(user)
            if user and bcrypt.check_password_hash(user.password, password):
                return {"message": "Login successfull"}
            else:
                return {"message": "Login unsuccessful"}
        except Exception as e:
            logger.error("some error occured", exc_info=e)
            return {"message": "an error occured "}
