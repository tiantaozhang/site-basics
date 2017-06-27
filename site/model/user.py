
from flask import current_app
from sqlalchemy import Integer, String
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from site import db
from passlib.apps import custom_app_context as pwd_context



class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"schema": "ep_ep"}

    primary_key = 'id'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    nickname = db.Column(String)
    pwd_hash = db.Column('password_hash', String)
    status = db.Column(Integer)
    updated_time = db.Column(db.DateTime)

    def hash_password(self, password):
        self.pwd_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.pwd_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer()
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer()
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data[data['id']])
        return user



