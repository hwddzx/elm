from flask import render_template, request, session, redirect, url_for
from apps.cms import cms_bp
from apps.forms.auth_forms import LoginForm, RegisterForm
from apps.models.auth_model import Auth, db


@cms_bp.route('/', endpoint='index')
def index():
    """主页"""
    return render_template('auth/index.html')


@cms_bp.route('/login/', methods=['GET', 'POST'])
def login():
    """登录"""
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        # 根据账号获取模型对象
        d1 = db.session.query(Auth).filter_by(username=username).first()
        # 判断密码是否正确
        if password == d1.password:
            # 设置session
            session['uid'] = username
            return redirect(url_for('cms.index'))
        else:
            return 'not ok'
    return render_template('auth/login.html', form=form, flags='登录', height=360)


@cms_bp.route('/register/', methods=['POST', 'GET'])
def register():
    """注册"""
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            u1 = Auth()
            u1.username = form.username.data
            u1.password = form.password.data
            db.session.add(u1)
            db.session.commit()
        except:
            return '用户名已存在'
        return 'ok'
    return render_template('auth/login.html', form=form, flags='注册', height=450)


@cms_bp.route('/logout/')
def logout():
    # 删除session
    session.clear()
    return redirect(url_for('cms.login'))
