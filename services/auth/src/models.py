from app import db
from datetime import datetime
from ulid import new as generate_ulid
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.sql import func


class ULIDType(TypeDecorator):
    impl = CHAR(26)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            return str(value)

    def process_result_value(self, value, dialect):
        if value is not None:
            return value


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean(), server_default="true", index=True)
    created_date = db.Column(db.DateTime(), server_default=func.now())
    updated_date = db.Column(
        db.DateTime(),
        server_default=func.now(),
        server_onupdate=func.now(),
        onupdate=func.now(),
    )
    created_by_id = db.Column(db.String(500), nullable=True, index=True)
    updated_by_id = db.Column(db.String(500), nullable=True, index=True)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"


# signup_model=swagger_api.model


class User(BaseModel):
    internal_id = db.Column(
        ULIDType, unique=True, index=True, default=lambda: str(generate_ulid())
    )
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.username}"

    @classmethod
    def get_user(cls, **criteria):
        return cls.query.filter_by(**criteria, is_active=True)
    