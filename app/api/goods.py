from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, reqparse, fields

from app.api._parser import paginate_parser, paginate_schema_base
from app.controller.goods import (
    get_goods_list, create_goods, get_goods_detail,
    delete_goods, get_goods_all
)

ns = Namespace("goods", description='货品')

# parser
goods_parser = reqparse.RequestParser()
goods_parser.add_argument("name", type=str, help='名称', location='json')
goods_parser.add_argument("g_type", type=str, help='型号', location='json')

# schema
goods_schema = ns.model('Goods', {
    'id': fields.Integer(description='ID'),
    'name': fields.String(description='货品名'),
    'g_type': fields.String(description='货品型号'),
    'total': fields.Integer(description='库存数'),
    'cost_price': fields.Float(description='成本总价'),
    'sales_price': fields.Float(description='成本总价')
})
goods_paginate_schema = ns.clone('GoodsPaginate', paginate_schema_base, {
    'items': fields.List(fields.Nested(goods_schema), description='数据')
})


@ns.route('/')
class GoodsList(Resource):
    """货品"""

    method_decorators = [jwt_required]

    @ns.expect(paginate_parser)
    @ns.marshal_with(goods_paginate_schema)
    def get(self):
        """获取货品列表"""
        page_info = paginate_parser.parse_args()
        return get_goods_list(page_info)

    @ns.expect(goods_parser)
    @ns.marshal_with(goods_schema)
    def post(self):
        """创建货品"""
        args = goods_parser.parse_args()
        return create_goods(args)


@ns.route('/all')
class GoodsAll(Resource):
    """所有货品"""

    method_decorators = [jwt_required]

    @ns.marshal_list_with(goods_schema)
    def get(self):
        """获取所有货品信息"""
        return get_goods_all()


@ns.route('/<int:gid>')
class GoodsDetail(Resource):
    """货品详情"""

    method_decorators = [jwt_required]

    @ns.marshal_with(goods_schema)
    def get(self, gid):
        """查询货品详情"""
        return get_goods_detail(gid)

    @ns.marshal_with(goods_schema)
    def delete(self, gid):
        """删除货品"""
        return delete_goods(gid)
