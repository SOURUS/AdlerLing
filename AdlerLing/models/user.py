from utilities.db import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    creation_date = db.Column(db.TIMESTAMP, default=datetime.utcnow(), nullable=False)
    isActivated = db.Column(db.Boolean,  unique=False, default=False, nullable=False)
    roles = db.relationship("RoleModel", secondary="userRoles", lazy='dynamic')

    @classmethod
    def find_by_email(cls, email) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
