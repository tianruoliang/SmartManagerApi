from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, reqparse, fields

from app.controller.goods import (
    get_goods_list, create_goods, get_goods_detail,
    get_goods_in_list, get_goods_out_list,
    create_goods_in, create_goods_out
)

ns = Namespace("goods", description='Goods Resource')

# parser
goods_parser = reqparse.RequestParser()
goods_parser.add_argument("name", type=str, help='名称', location='json')
goods_parser.add_argument("g_type", type=str, help='型号', location='json')
goods_parser.add_argument("total", type=int, required=False, help='库存数', location='json')

goods_action_parser = reqparse.RequestParser()
goods_action_parser.add_argument('number', type=int, help='number', location='json')
goods_action_parser.add_argument('staff_id', type=int, help='staff_id', location='json')
goods_action_parser.add_argument('company_id', type=int, help='company_id', location='json')

# schema
goods_schema = ns.model('Goods', {
    'id': fields.Integer,
    'name': fields.String,
    'g_type': fields.String,
    'total': fields.Integer
})


@ns.route('/')
class GoodsList(Resource):
    method_decorators = [jwt_required]

    @ns.marshal_list_with(goods_schema)
    def get(self):
        return get_goods_list()

    @ns.expect(goods_parser)
    @ns.marshal_with(goods_schema)
    def post(self):
        args = goods_parser.parse_args()
        return create_goods(args)


@ns.route('/<int:gid>')
class GoodsDetail(Resource):
    method_decorators = [jwt_required]

    @ns.marshal_with(goods_schema)
    def get(self, gid):
        return get_goods_detail(gid)


@ns.route('/<int:gid>/<string:action>')
class GoodsAction(Resource):
    method_decorators = [jwt_required]

    def get(self, gid, action):
        if action == 'in':
            return get_goods_in_list(gid)
        else:
            return get_goods_out_list(gid)

    @ns.expect(goods_action_parser)
    def post(self, gid, action):
        args = goods_action_parser.parse_args()
        if action == 'in':
            create_goods_in(gid, args)
        else:
            create_goods_out(gid, args)
