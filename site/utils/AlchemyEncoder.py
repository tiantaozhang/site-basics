# coding=utf-8
from flask import json

from decimal import Decimal
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.state import InstanceState


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, Decimal):
                        data = float(data)
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
        try:
            if isinstance(obj, Decimal):
                obj = float(obj)
            if isinstance(obj, InstanceState):
                return None
        except TypeError:
                return None
        return json.JSONEncoder.default(self, obj)
