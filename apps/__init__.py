from flask import Flask


def register_cms_bp(app: Flask):
    """注册蓝图"""
    from apps.cms import cms_bp
    app.register_blueprint(cms_bp)


def register_db(app: Flask):
    """注册模型"""
    from apps.models import db
    db.init_app(app)


def init_session(app: Flask):
    """初始化session"""
    from flask_session import Session
    Session(app)


def init_login_manager(app: Flask):
    from apps.tools.login_tools import login_manager
    login_manager.init_app(app)


def create_cms_app(config_str: str):
    # 实例化Flask对象
    app = Flask(__name__)
    # 添加配置文件
    app.config.from_object(config_str)
    # 初始化session
    init_session(app)
    # 注册模型
    register_db(app)
    # 初始化登录manager
    init_login_manager(app)
    # 注册蓝图
    register_cms_bp(app)
    return app
