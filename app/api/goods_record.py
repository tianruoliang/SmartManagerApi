from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, reqparse, fields

from app.api._parser import paginate_parser, paginate_schema_base
from app.controller.goods_record import (
    get_goods_record_list, create_goods_record
)

ns = Namespace("goods_record", description='进出库记录')

# parser
goods_record_parser = reqparse.RequestParser()
goods_record_parser.add_argument('number', type=int, help='number', location='json')
goods_record_parser.add_argument('goods_id', type=int, help='goods_id', location='json')
goods_record_parser.add_argument('staff_id', type=int, help='staff_id', location='json')
goods_record_parser.add_argument('company_id', type=int, help='company_id', location='json')
goods_record_parser.add_argument("g_type", type=str, help='action', location='json')
goods_record_parser.add_argument("single_price", type=float, help='单价', location='json')
goods_record_parser.add_argument("record", type=str, required=False, help='备注记录', location='json')

# schema
goods_record_schema = ns.model('GoodsAction', {
    'id': fields.Integer(description='ID'),
    'goods_name': fields.String(description='货品名'),
    'goods_g_type': fields.String(description='货品型号'),
    'number': fields.Integer(description='数量'),
    'record': fields.String(description='记录备注'),
    'g_type': fields.String(desciption='动作'),
    'single_price': fields.Float(desciption='单价（元）'),
    'create_time': fields.DateTime(description='操作时间'),
    'staff': fields.String(description='经手人'),
    'company': fields.String(description='公司')
})
goods_record_paginate_schema = ns.clone('GoodsActionPaginate', paginate_schema_base, {
    'items': fields.List(fields.Nested(goods_record_schema), description='数据')
})


@ns.route('/')
class GoodsRecordList(Resource):
    """货品入库/出库"""

    # method_decorators = [jwt_required]

    @ns.expect(paginate_parser)
    @ns.marshal_with(goods_record_paginate_schema)
    def get(self):
        """获取货品出/入库记录"""
        page_info = paginate_parser.parse_args()
        return get_goods_record_list(page_info)

    @ns.expect(goods_record_parser)
    @ns.marshal_with(goods_record_schema)
    def post(self):
        """增加货品出/入库记录"""
        args = goods_record_parser.parse_args()
        return create_goods_record(args)
