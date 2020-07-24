import datetime
import os

here = os.path.dirname(__file__)
project_path = os.path.join(here, os.pardir)


class Config:
    DEBUG = True
    JWT_IDENTITY_CLAIM = 'sub'
    JWT_BLACKLIST_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=30)
    LOG_PATH = os.path.join(project_path, "logs")
    ERROR_INCLUDE_MESSAGE = False
    PROPAGATE_EXCEPTIONS = True


class DevConfig(Config):
    SECRET_KEY = "development"
    JWT_SECRET_KEY = "development"
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % os.path.join(project_path, "dev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", b'S\xe2\x83\xa0\x12\x19o\r\x14\xd2.\xb4y\xbc\xda\x93')
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", b'\xff\xd0\x06\xb3\x15r\x1a\xc2\xaa\xb9H\x9d<\xfd\x0f}')
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI",
                                        "sqlite:///%s" % os.path.join(project_path, "prod.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CONF_MAPPING = {
    "development": DevConfig,
    "production": ProdConfig
}
