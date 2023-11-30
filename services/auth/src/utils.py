from app import db, bcrypt
from models import User



class UserManager:

    def signup(self, data):
        if not data:
            return {"message": "No input data provided"}
        email = data.get("email")
        user = User.get_user(email=email).first()

        if user == None:
            hashed_password = bcrypt.generate_password_hash(data.get("password")).decode(
                "utf-8"
            )
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
        return {"message": "enter different email"}

class LoginManager:

    def login(self, data):
        email = data.get("email")
        password = data.get("password")
        user = User.get_user(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return {"message": "Login successfull"}
        else:
            return {"message": "Login unsuccessful"}
