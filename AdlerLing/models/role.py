from utilities.db import db
from sqlalchemy.orm import relationship
from models.user_role import UserRoleModel


class RoleModel(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    @classmethod
    def find_by_name(cls, name) -> "RoleModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
