from flask import render_template, request, session, redirect, url_for
from flask_login import login_user, current_user, logout_user
from apps.cms import cms_bp
from apps.forms.auth_forms import LoginForm, RegisterForm
from apps.models.auth_model import Auth, db


@cms_bp.route('/', endpoint='index')
def index():
    """主页"""
    if current_user.is_authenticated:
        print(current_user.username)
    return render_template('auth/index.html')


@cms_bp.route('/login/', methods=['GET', 'POST'])
def login():
    """登录"""
    error = ''
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # 根据账号获取模型对象
        u1 = Auth.query.filter_by(username=form.username.data).first()
        # 判断密码是否正确
        if u1.check_password(form.password.data):
            # 设置session
            # session['uid'] = form.username.data
            login_user(u1)
            return redirect(url_for('cms.index'))
        error = '用户名或密码错误!'
    return render_template('auth/login.html', form=form, flags='登录', height=400, error=error)


@cms_bp.route('/register/', methods=['POST', 'GET'])
def register():
    """注册"""
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        u1 = Auth()
        u1.set_attr(form.data)
        db.session.add(u1)
        db.session.commit()
        return redirect(url_for('cms.login'))
    return render_template('auth/login.html', form=form, flags='注册', height=480)


@cms_bp.route('/logout/')
def logout():
    # 删除session
    # session.clear()
    logout_user()
    return redirect(url_for('cms.login'))
