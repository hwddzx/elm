class DevConfig:
    DEBUG = True
    SECRET_KEY = 'a123b'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1:3306/elm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
