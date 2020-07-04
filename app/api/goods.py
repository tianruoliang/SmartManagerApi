from flask_restx import Namespace, Resource, reqparse, fields

from app.controller.goods import get_goods_list, create_goods, get_goods_detail

ns = Namespace("goods", description='Goods Resource')
# parser
goods_parser = reqparse.RequestParser()
goods_parser.add_argument("name", type=str, help='名称', location='json')
goods_parser.add_argument("g_type", type=str, help='型号', location='json')
goods_parser.add_argument("total", type=int, required=False, help='库存数', location='json')

goods_in_parser = reqparse.RequestParser()
goods_in_parser.add_argument('number', type=int, help='number', location='json')

goods_out_parser = reqparse.RequestParser()
goods_out_parser.add_argument('number', type=int, help='number', location='json')

# schema
goods_schema = ns.model('Goods', {
    'id': fields.Integer,
    'name': fields.String,
    'total': fields.Integer,
    'create_time': fields.DateTime
})


@ns.route('/')
class GoodsList(Resource):
    @ns.marshal_list_with(goods_schema)
    def get(self):
        return get_goods_list()

    @ns.expect(goods_parser)
    @ns.marshal_with(goods_schema, code=201)
    def post(self):
        args = goods_parser.parse_args()
        return create_goods(args), 201


@ns.route('/<int:gid>')
class GoodsDetail(Resource):
    @ns.marshal_with(goods_schema)
    def get(self, gid):
        return get_goods_detail(gid)
