from . import db, ma
from datetime import datetime


class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    token = db.Column(db.Text, nullable=False)
    loged_at = db.Column(db.DateTime, nullable=False,
                         default=datetime.now())

    def __init__(self, name, email, password, token):
        self.name = name
        self.email = email
        self.password = password
        self.token = token


class user(ma.Schema):
    class Meta:
        fields = ('name', 'email')


user_schemas = user(many=True)
user_schema = user()
