from flask_restful import Resource
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt
)

from marshmallow import ValidationError
from schemas.user import UserSchema
from models.user import UserModel
from models.role import RoleModel
from utilities.blacklist import BLACKLIST
from utilities.role_checker import check_roles

user_schema = UserSchema()


class UserRegister(Resource):
    def post(self):
        try:
            user = user_schema.load(request.get_json(), partial=("roles", "isActivated"))
        except ValidationError as err:
            return err.messages, 400

        if UserModel.find_by_email(user.email):
            return {
                "message": "A user with that email already exists."
            }, 400

        user.password = generate_password_hash(user.password)
        role = RoleModel.find_by_name("student")
        user.roles.append(role)

        user.save_to_db()

        return {"message": "User created successfully."}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        return user_schema.dump(user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": "User not found."}, 404
        user.delete_from_db()
        return {"message": "User deleted."}, 200


class UserLogin(Resource):
    def post(self):
        try:
            user_data = user_schema.load(request.get_json(), partial=("roles", "isActivated"))
        except ValidationError as err:
            return err.messages, 400

        user = UserModel.find_by_email(user_data.email)
        dumpUser = user_schema.dump(user)

        if user and check_password_hash(user.password, user_data.password):
            access_token = create_access_token(identity=dumpUser, fresh=True)
            refresh_token = create_refresh_token(identity=dumpUser)

            ret = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            return ret, 200

        return {"message": "Invalid credentials!"}, 401


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()["jti"]
        user = get_jwt_identity()
        BLACKLIST.add(jti)
        return {
            "message": "User <id={}> successfully logged out.".format(user["id"])
        }, 200


class UserCheck(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()["jti"]
        user = get_jwt_identity()
        return {
            "message": "User checking".format(user["id"])
        }, 200


class AdminCheck(Resource):
    @jwt_required
    @check_roles(['admin'])
    def post(self):

        user = get_jwt_identity()
        return {
            "message": "User checking".format(user["id"])
        }, 200


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
