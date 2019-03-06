from utilities.ma import ma
from models.role import RoleModel


class RoleSchema(ma.ModelSchema):
    class Meta:
        model = RoleModel
        dump_only = ("creation_date",)
