import os
from redis import Redis


def get_db_dir():
    path = os.path.dirname(os.path.dirname(__file__))
    return 'sqlite:///{}/elm.db'.format(path)


class DevConfig:
    DEBUG = True
    SECRET_KEY = 'a123b'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/elm'
    # SQLALCHEMY_DATABASE_URI = get_db_dir()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置redis
    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis(host='127.0.0.1', port=6379)
    SESSION_KEY_PREFIX = 'ddzx:'
