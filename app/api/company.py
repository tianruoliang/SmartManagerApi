from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, reqparse, fields

from app.api._parser import paginate_parser, paginate_schema_base
from app.controller.company import (
    get_company_list, create_company, get_company_all,
    get_company_detail, delete_company, put_company
)

ns = Namespace('company', description='合作公司')

# parser
create_parser = reqparse.RequestParser()
create_parser.add_argument('name', type=str, help='公司名', location='json')
create_parser.add_argument('c_type', help='公司类型', location='json')
create_parser.add_argument('phone', type=str, help='联系电话', location='json')
create_parser.add_argument('address', type=str, help='联系地址', location='json')

# schema
company_schema = ns.model('Company', {
    'id': fields.Integer(description='ID'),
    'name': fields.String(description='公司名'),
    'phone': fields.String(description='电话'),
    'c_type': fields.String(description='合作方式'),
    'address': fields.String(description='地址'),
    'active': fields.Boolean(description='状态'),
    'create_time': fields.DateTime(description='创建时间')
})
paginate_schema = ns.clone('CompanyPaginate', paginate_schema_base, {
    'items': fields.List(fields.Nested(company_schema), description='数据')
})


@ns.route('/')
class CompanyList(Resource):
    """公司"""
    method_decorators = [jwt_required]

    @ns.expect(paginate_parser)
    @ns.marshal_with(paginate_schema)
    def get(self):
        """批量获取公司信息"""
        page_info = paginate_parser.parse_args()
        return get_company_list(page_info)

    @ns.expect(create_parser)
    @ns.marshal_with(company_schema)
    def post(self):
        """创建公司"""
        args = create_parser.parse_args()
        return create_company(args)


@ns.route('/all')
class CompanyAll(Resource):
    """所有公司"""

    method_decorators = [jwt_required]

    @ns.marshal_list_with(company_schema)
    def get(self):
        """获取所有公司信息"""
        return get_company_all()


@ns.route('/<int:cid>')
class CompanyDetail(Resource):
    """公司详情"""
    method_decorators = [jwt_required]

    @ns.marshal_with(company_schema)
    def get(self, cid):
        """查询公司信息"""
        return get_company_detail(cid)

    @ns.marshal_with(company_schema)
    def delete(self, cid):
        """删除公司"""
        return delete_company(cid)

    @ns.expect(create_parser)
    @ns.marshal_with(company_schema)
    def put(self, cid):
        """更新公司信息"""
        args = create_parser.parse_args()
        return put_company(cid, args)
