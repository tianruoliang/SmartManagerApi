from flask_jwt_extended import jwt_required, get_current_user
from flask_restx import Namespace, Resource, reqparse, fields

from app.controller.user import get_user_list

ns = Namespace('user', description='User Resource')

# parser
create_parser = reqparse.RequestParser()
create_parser.add_argument('name', type=str, help='姓名', location='json')
create_parser.add_argument('username', type=str, help='用户名', location='json')
create_parser.add_argument('password', type=str, help='密码', location='json')
create_parser.add_argument('phone', type=str, help='联系电话', location='json')
create_parser.add_argument('role_id', help='职位ID', location='json')

# schema
user_schema = ns.model('User', {
    'id': fields.Integer,
    'name': fields.String,
    'username': fields.String,
    'phone': fields.String,
    'role': fields.String,
    'create_time': fields.DateTime
})


@ns.route('/')
class UserList(Resource):
    method_decorators = [jwt_required]

    @ns.marshal_list_with(user_schema)
    def get(self):
        return get_user_list()


@ns.route('/me')
class UserDetail(Resource):
    method_decorators = [jwt_required]

    @ns.marshal_with(user_schema)
    def get(self):
        user = get_current_user()
        return user.to_dict()
