from utilities.ma import ma
from models.user import UserModel
from schemas.role import RoleSchema


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
    roles = ma.Nested(RoleSchema, many=True, required=True)
