from utilities.db import db
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, backref


class UserRoleModel(db.Model):
    __tablename__ = 'userRoles'
    user_id = db.Column(Integer, ForeignKey('users.id'), primary_key=True)
    role_id = db.Column(Integer, ForeignKey('roles.id'), primary_key=True)

    user = relationship('UserModel', backref=backref('RoleModel', cascade="all, delete-orphan"))
    role = relationship('RoleModel', backref=backref('UserModel', cascade="all, delete-orphan"))
