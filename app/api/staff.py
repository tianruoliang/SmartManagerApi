from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields, reqparse

from app.controller.staff import get_staff_list, create_staff, get_staff_detail, delete_staff_detail

ns = Namespace("staff", description="Staff Resource")

# parser
staff_parser = reqparse.RequestParser()
staff_parser.add_argument("name", type=str, help='姓名', location='json')
staff_parser.add_argument("gender", type=str, help='性别', location='json')
staff_parser.add_argument("phone", type=str, help='电话', location='json')

# schema
staff_schema = ns.model('Staff', {
    'id': fields.Integer,
    'name': fields.String,
    'gender': fields.String,
    'phone': fields.String
})


@ns.route('/')
class StaffList(Resource):
    method_decorators = [jwt_required]

    @ns.marshal_list_with(staff_schema)
    def get(self):
        return get_staff_list()

    @ns.expect(staff_parser)
    @ns.marshal_with(staff_schema)
    def post(self):
        args = staff_parser.parse_args()
        return create_staff(args)


@ns.route('/<int:sid>')
class StaffDetail(Resource):
    method_decorators = [jwt_required]

    @ns.marshal_with(staff_schema)
    def get(self, sid):
        return get_staff_detail(sid)

    @ns.marshal_with(staff_schema)
    def delete(self, sid):
        return delete_staff_detail(sid)
