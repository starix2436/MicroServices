from .app import db
from datetime import datetime 

class BaseModel(db.Model):
    __abstract__ = True
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean(), server_default="true", index=True)
    created_date = db.Column(db.DateTime(), server_default=datetime.utcnow())
    updated_date = db.Column(db.DateTime(), server_default=datetime.utcnow(), server_onupdate=datetime.utcnow(), onupdate=datetime.utcnow())
    created_by_id = db.Column(db.String(500), nullable=True, index=True)
    updated_by_id = db.Column(db.String(500), nullable=True, index=True)
 
    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"