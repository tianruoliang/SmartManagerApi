import logging
import os
from logging import handlers


def init_logger(app):
    logging.basicConfig(level=logging.DEBUG)
    log_dir = app.config["LOG_PATH"]
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    log_path = os.path.join(log_dir, "SmartManagerApi.log")
    fh = handlers.RotatingFileHandler(log_path, maxBytes=1024 * 100, backupCount=10)
    fh.setLevel(logging.INFO)
    fh_fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    fh.setFormatter(logging.Formatter(fmt=fh_fmt))
    app.logger.addHandler(fh)
