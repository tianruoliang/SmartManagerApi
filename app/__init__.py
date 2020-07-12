from flask import Flask

from app.api import bp as api_bp
from app.auth.view import bp as auth_bp
from app.cli import init_cli
from app.config import CONF_MAPPING
from app.log import init_logger
from app.plugin import db, jwt


def create_app(conf_name):
    app = Flask(__name__)
    # load config
    app.config.from_object(CONF_MAPPING[conf_name])
    # init logger
    init_logger(app)
    # init plugin
    db.init_app(app)
    jwt.init_app(app)
    # register blueprint
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)
    # init cli
    init_cli(app)
    return app
