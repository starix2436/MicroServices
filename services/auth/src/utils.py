from app import db, bcrypt
from models import User
from loggers import logger
from flask import request


class UserManager:
    def __init__(self, request):
        args = request.args
        self.first_name = args.get("first name")
        self.last_name = args.get("last name")
        self.username = args.get("username")
        self.email = args.get("email")

    def filter(self, user):
        try:
            if self.first_name:
                user = User.query.filter(User.first_name == self.first_name)
                return user

            if self.last_name:
                user = User.query.filter(User.last_name == self.last_name)
                return user

            if self.username:
                user = User.query.filter(User.username == self.username)
                return user

            if self.email:
                user = User.query.filter(User.email == self.email)
                return user

            return user

        except Exception as e:
            logger.error("some error occured", exc_info=e)
            return []

    def details(self, id):
        user = User.get_user(id=id).first()
        # show phone numbers also
        return user

    def alldetails(self):
        user = User.get_user().all()
        return self.filter(user)

    def filtername(self, filter_name):
        user = User.get_user(first_name=filter_name)
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


class UpdateManager:
    def update(self, id, data):
        update_data = User.get_user(id=id).first()
        if not update_data:
            return "user id doesnot exist"

        update_data.username = data.get("username", update_data.username)
        update_data.email = data.get("email", update_data.email)
        update_data.first_name = data.get("first_name", update_data.first_name)
        update_data.last_name = data.get("last_name", update_data.last_name)

        db.session.commit()
        return {"message": "data updated"}


class DeleteManager:
    def delete(self, id):
        delete_user = User.get_user(id=id).first()
        if not delete_user:
            return "user id doesnot exist"
        db.session.delete(delete_user)
        db.session.commit()
        return {"message": "deleted successfully"}
