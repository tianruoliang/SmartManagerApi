from flask import Blueprint
from flask import request
from flask_restx import Api
from werkzeug.exceptions import HTTPException

from .company import ns as company_ns
from .goods import ns as goods_ns
from .role import ns as role_ns
from .staff import ns as staff_ns
from .user import ns as user_ns

bp = Blueprint('api', __name__, url_prefix='/smart-manager/api')

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}
api = Api(
    bp, version='1.0', title='Smart Manager API',
    description='Smart Manager API Doc',
    security='Bearer Auth',
    authorizations=authorizations
)


@api.errorhandler(HTTPException)
def api_http_exception(error):
    api.logger.error(
        f"{error.data}\n[remote_addr]: {request.remote_addr}\n"
        f"[method]: {request.method}\n[url]: {request.url}\n"
        f"[data]: {request.form}"
    )
    return error.data, error.code




api.add_namespace(user_ns)
api.add_namespace(company_ns)
api.add_namespace(role_ns)
api.add_namespace(goods_ns)
api.add_namespace(staff_ns)
