from app import db 
from models import User

def signup(data):
    if not data:
        return {"message": "No input data provided"}
    email = data.get("email")
    user = User.get_user(email=email).first()
  
    if user == None:
        new_acc = User(
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
            )
        db.session.add(new_acc)
        db.session.commit()
        return {"message": "success"}
    return {"message": "enter different email"}
    
        
  
