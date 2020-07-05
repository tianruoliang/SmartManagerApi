from flask_restx import Namespace, Resource, fields

from app.controller.role import get_role_list

ns = Namespace("role", description="Role Resource")
# schema
role_schema = ns.model('Role', {
    'id': fields.Integer,
    'name': fields.String
})


@ns.route('/')
class RoleList(Resource):
    @ns.marshal_list_with(role_schema)
    def get(self):
        return get_role_list()
