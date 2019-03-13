from flask_sqlalchemy import SQLAlchemy

# 实例化模型对象
db = SQLAlchemy()


class BaseModel(db.Model):
    """定义模型基类"""
    # 修饰类，会使这个类成为一个抽象类，这个类将不能生成对象实例，但可以做为对象变量声明的类型
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    is_status = db.Column(db.Integer, default=1)


from . import auth_model
