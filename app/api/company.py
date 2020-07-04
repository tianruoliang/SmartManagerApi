from flask_restx import Namespace, Resource, reqparse, fields

from app.controller.company import get_company_list, create_company, get_company_detail, delete_company

ns = Namespace('company', description='Company Resource')

# parser
create_parser = reqparse.RequestParser()
create_parser.add_argument('name', type=str, help='公司名', location='json')
create_parser.add_argument('c_type', help='公司类型', location='json')
create_parser.add_argument('phone', type=str, help='联系电话', location='json')
create_parser.add_argument('address', type=str, help='联系地址', location='json')

# schema
company_schema = ns.model('Company', {
    'id': fields.Integer,
    'name': fields.String,
    'phone': fields.String,
    'c_type': fields.String,
    'address': fields.String,
    'create_time': fields.DateTime
})


@ns.route('/')
class CompanyList(Resource):
    @ns.marshal_list_with(company_schema)
    def get(self):
        return get_company_list()

    @ns.expect(create_parser)
    @ns.marshal_with(company_schema, code=201)
    def post(self):
        args = create_parser.parse_args()
        return create_company(args), 201


@ns.route('/<int:cid>')
class CompanyDetail(Resource):
    @ns.marshal_with(company_schema)
    def get(self, cid):
        return get_company_detail(cid)

    @ns.marshal_with(company_schema, code=204)
    def delete(self, cid):
        return delete_company(cid), 204
