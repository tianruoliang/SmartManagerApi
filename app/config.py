import os

here = os.path.dirname(__file__)
project_path = os.path.join(here, os.pardir)


class DevConfig:
    DEBUG = True
    SECRET_KEY = "development"
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % os.path.join(project_path, "dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    LOG_PATH = os.path.join(project_path, "logs")
    ERROR_INCLUDE_MESSAGE = False


class ProdConfig:
    DEBUG = True
    SECRET_KEY = b"\x94'\xe7\xd8!\xd0-\x80\xdbY*\xa8\xdb\xb9\x98DnMv\xf6\xb8hYa"
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % os.path.join(project_path, "prod.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_PATH = os.path.join(project_path, "logs")
    ERROR_INCLUDE_MESSAGE = False


CONF_MAPPING = {
    "development": DevConfig,
    "production": ProdConfig
}
