from flask_login import LoginManager
from apps.models.auth_model import Auth

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return Auth.query.get(int(user_id))
