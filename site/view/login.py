
import requests
from flask import request, jsonify, session, g, url_for
from site.view import main
from site.view.exception import BadRequest, YMException
from site.model.user import User
from site import db, auth


@main.route('/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        BadRequest(YMException(message=u'用户名或密码为空'))
    if User.query.filter_by(name=username).first() is not None:
        BadRequest(YMException(message=u'用户已经存在'))
    user = User(name=username, nickname=username, status=1)
    user.hash_password(password)

    db.session.add(user)
    db.session.commit()
    return (jsonify({'code': 0, 'data': {'username': user.name}}), 201, {
            'Location': url_for('get_user', id=user.id, _external=True)})


@main.route('/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        BadRequest(YMException(message=u"不存在"))
    return jsonify({'code': 0, 'data': {'username': user.name}}), 200


@main.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'code': 0, 'token': token.decode(
        'ascii'), 'duration': 600}), 200


@main.route('resource')
@auth.login_required
def get_resource():
    return jsonify({'code': 0, 'data': 'Hello, %s!' % g.user.username}), 200
