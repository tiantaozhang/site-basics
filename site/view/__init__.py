import json
from flask import Blueprint
from cerberus import Validator

main = Blueprint("main", __name__)
main.config = {}

