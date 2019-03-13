from flask import render_template
from apps.cms import cms_bp


@cms_bp.route('/')
def index():
    return render_template('auth/login.html')
