from flask_restx import reqparse, Model, fields

# paginate parser
paginate_parser = reqparse.RequestParser()
paginate_parser.add_argument("page", type=int, required=False, help='当前页')
paginate_parser.add_argument("per_page", type=int, required=False, help='每页条数')

# paginate schema base
paginate_schema_base = Model('PaginateBase', {
    'page': fields.Integer(description='当前页'),
    'per_page': fields.Integer(description='每页条数'),
    'total': fields.Integer(description='总数')
})
