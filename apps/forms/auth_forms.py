from wtforms import Form, StringField, PasswordField, validators
from apps.models.auth_model import Auth, db


class LoginForm(Form):
    """登录form"""
    username = StringField(
        label='用户名:',
        validators=[
            validators.DataRequired(message='请输入用户名'),
            validators.Length(min=3, message='少于3个字符'),
            validators.Length(max=18, message='超出18个字符'),
        ],
        render_kw={'class': 'form-control', 'placeholder': '请输入用户名'}
    )

    password = PasswordField(
        label='密码:',
        validators=[
            validators.DataRequired(message='请输入密码'),
            validators.Length(min=6, message='少于6个字符'),
            validators.Length(max=18, message='超出18个字符'),
        ],
        render_kw={'class': 'form-control', 'placeholder': '请输入密码'}
    )


class RegisterForm(LoginForm):
    """注册form,继承了登录form"""
    password1 = PasswordField(
        label='确认密码:',
        validators=[
            validators.DataRequired(message='请输入密码'),
            validators.EqualTo('password', message='两次密码不一致')
        ],
        render_kw={'class': 'form-control', 'placeholder': '请确认密码'}
    )

    def validate_username(self, field):
        # 验证用户名是否存在
        if not db.session.query(Auth).filter_by(username=field.data).all() == []:
            raise validators.ValidationError(message='用户名已存在')
