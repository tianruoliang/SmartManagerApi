from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields, reqparse

from app.controller.staff import get_staff_list, create_staff, get_staff_detail, delete_staff_detail

ns = Namespace("staff", description="员工")

# parser
staff_parser = reqparse.RequestParser()
staff_parser.add_argument("name", type=str, help='姓名', location='json')
staff_parser.add_argument("gender", type=str, help='性别', location='json')
staff_parser.add_argument("phone", type=str, help='电话', location='json')

# schema
staff_schema = ns.model('Staff', {
    'id': fields.Integer(description='ID'),
    'name': fields.String(description='姓名'),
    'gender': fields.String(description='性别'),
    'phone': fields.String(description='电话')
})


@ns.route('/')
class StaffList(Resource):
    """员工"""
    # method_decorators = [jwt_required]

    @ns.marshal_list_with(staff_schema)
    def get(self):
        """批量查询员工"""
        return get_staff_list()

    @ns.expect(staff_parser)
    @ns.marshal_with(staff_schema)
    def post(self):
        """新增员工"""
        args = staff_parser.parse_args()
        return create_staff(args)


@ns.route('/<int:sid>')
class StaffDetail(Resource):
    """员工详情"""
    # method_decorators = [jwt_required]

    @ns.marshal_with(staff_schema)
    def get(self, sid):
        """获取员工详情"""
        return get_staff_detail(sid)

    @ns.marshal_with(staff_schema)
    def delete(self, sid):
        """删除员工"""
        return delete_staff_detail(sid)
