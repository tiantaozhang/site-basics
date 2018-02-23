# # coding=utf-8
# #
# from raven.contrib.flask import Sentry
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_httpauth import HTTPBasicAuth
#
# from config.config import *
#
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager_view = 'auth.login'
#
# db = SQLAlchemy()
# auth = HTTPBasicAuth()
#
# sentry_client = None
#
# s3 = None
#
#
# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(config[config_name])
#
#     app.json_encoder = AlchemyEncoder
#
#     # login_manager.init_app(app)
#     db.init_app(app)
#     # db.reflect(app=app)
#
#     # s3
#     global s3
#     s3 = boto3.resource(
#         's3',
#         region_name=AWS['region'],
#         aws_access_key_id=AWS['access_key_id'],
#         aws_secret_access_key=AWS['secret_access_key']
#     )
#
#     # init raven
#     global sentry_client
#     sentry_client = Sentry(app, dsn=config[config_name].SENTRY_DSN)
#
#     from admin.views import main as main_blueprint
#     app.register_blueprint(main_blueprint)
#
#     from admin.views.dsp import dsp as dsp_blueprint
#     app.register_blueprint(dsp_blueprint, url_prefix="/dsp")
#
#     from admin.views.dashboard.dashboard import blueprint as dashboard_blueprint
#     app.register_blueprint(dashboard_blueprint, url_prefix="/dashboard")
#
#     from admin.views.common_api.api import blueprint as common_api_blueprint
#     app.register_blueprint(common_api_blueprint, url_prefix="/common")
#
#     from admin.views.external_api.api import blueprint as external_api_blueprint
#     app.register_blueprint(external_api_blueprint, url_prefix="/external")
#
#     from admin.views.application import blueprint as application_blueprint
#     app.register_blueprint(application_blueprint, url_prefix="/app")
#
#     from admin.views.ader_interaction.api import blueprint as ader_interaction_blueprint
#     app.register_blueprint(ader_interaction_blueprint, url_prefix="/ader_interaction")
#
#     from admin.views.admin import blueprint as admin_blueprint
#     app.register_blueprint(admin_blueprint, url_prefix="/admin")
#
#     return app
