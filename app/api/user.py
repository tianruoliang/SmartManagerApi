from flask_restx import Namespace, Resource, reqparse, fields, abort

from app.controller.user import get_user_list, create_user, get_user_detail, delete_user

ns = Namespace('user', description='User Resource')

# parser
create_parser = reqparse.RequestParser()
create_parser.add_argument('username', type=str, help='姓名', location='json')
create_parser.add_argument('phone', type=str, help='联系电话', location='json')
create_parser.add_argument('role_id', help='职位ID', location='json')

# schema
user_schema = ns.model('User', {
    'id': fields.Integer,
    'username': fields.String,
    'phone': fields.String,
    'role': fields.String,
    'create_time': fields.DateTime
})


@ns.route('/')
class UserList(Resource):

    @ns.marshal_list_with(user_schema)
    def get(self):
        return get_user_list()

    @ns.expect(create_parser)
    @ns.marshal_list_with(user_schema, code=201)
    def post(self):
        abort(404, 'no')
        args = create_parser.parse_args()
        return create_user(args), 201


@ns.route('/<uid>')
class UserDetail(Resource):

    @ns.marshal_with(user_schema)
    def get(self, uid):
        return get_user_detail(uid)

    @ns.marshal_with(user_schema, code=204)
    def delete(self, uid):
        return delete_user(uid), 204
