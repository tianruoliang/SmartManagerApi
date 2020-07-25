from flask_restx import Namespace, Resource, fields

from app.controller.role import get_role_list

ns = Namespace("role", description="角色")

# schema
role_schema = ns.model('Role', {
    'id': fields.Integer(description='ID'),
    'name': fields.String(description='角色名')
})


@ns.route('/')
class RoleList(Resource):
    """角色"""

    @ns.marshal_list_with(role_schema)
    def get(self):
        """批量查询角色"""
        return get_role_list()
