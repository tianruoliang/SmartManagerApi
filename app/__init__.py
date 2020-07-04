import logging
import os
from logging import handlers

from flask import Flask

from app.api import bp
from app.config import CONF_MAPPING
from app.model import db
from app.model.user import Role


def create_app(conf_name):
    app = Flask(__name__)
    # load config
    app.config.from_object(CONF_MAPPING[conf_name])
    # init logger
    logging.basicConfig(level=logging.DEBUG)
    log_dir = CONF_MAPPING[conf_name].LOG_PATH
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    log_path = os.path.join(log_dir, "smart-manager.log")
    fh = handlers.RotatingFileHandler(log_path, maxBytes=1024 * 100, backupCount=10)
    fh.setLevel(logging.INFO)
    fh_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    fh.setFormatter(logging.Formatter(fmt=fh_fmt))
    app.logger.addHandler(fh)
    # init plugin
    db.init_app(app)
    # register blueprint
    app.register_blueprint(bp)

    @app.cli.command("init-db")
    def init_db():
        db.drop_all()
        db.create_all()
        Role.init_role()

    return app
