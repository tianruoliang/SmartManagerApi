import os

here = os.path.dirname(__file__)
project_path = os.path.join(here, os.pardir)


class Config:
    DEBUG = True
    JWT_IDENTITY_CLAIM = 'sub'
    JWT_BLACKLIST_ENABLED = True
    LOG_PATH = os.path.join(project_path, "logs")
    ERROR_INCLUDE_MESSAGE = False


class DevConfig(Config):
    SECRET_KEY = "development"
    JWT_SECRET_KEY = "development"
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % os.path.join(project_path, "dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = b"\x94'\xe7\xd8!\xd0-\x80\xdbY*\xa8\xdb\xb9\x98DnMv\xf6\xb8hYa"
    JWT_SECRET_KEY = b'<\xa3=\xaf\xd9\xa9\x19\xa0\xe7\xedr\xdf\x0c\x1a\xfa\x8f\x8c\xfd\xbeF\xc7\x15a\xe7'
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % os.path.join(project_path, "prod.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CONF_MAPPING = {
    "development": DevConfig,
    "production": ProdConfig
}
