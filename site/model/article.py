
from sqlalchemy import Integer, String
from site import db


class Article(db.Model):
    __tablename__ = "article"
    __table_args__ = {"schema": "ep_ep"}

    primary_key = 'id'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String)
    description = db.Column(String)
    cover = db.Column('cover_img', String)
    content = db.Column(String)
    status = db.Column(Integer)
    updated_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime)
