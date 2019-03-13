from apps.models import BaseModel, db


class Auth(BaseModel):
    username = db.Column(db.String(16), unique=True, index=True)
    password = db.Column(db.String(128), nullable=False)
