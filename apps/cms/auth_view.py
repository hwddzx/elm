from flask import render_template, request
from apps.cms import cms_bp
from apps.forms.auth_forms import LoginForm, RegisterForm


@cms_bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        return 'ok'
    return render_template('auth/login.html', form=form, flags='登录')


@cms_bp.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return 'ok'
    return render_template('auth/login.html', form=form, flags='注册')
