
from sqlalchemy import Integer, String
from site import db


class Tag(db.Model):
    __tablename__ = "tag"
    __table_args__ = {"schema": "ep_ep"}

    primary_key = 'id'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    parent = db.Column(Integer)
