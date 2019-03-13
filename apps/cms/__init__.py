from flask import Blueprint

# 实例化蓝图对象
cms_bp = Blueprint('cms', __name__)

from . import auth_view
