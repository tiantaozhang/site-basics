import os
from datetime import timedelta

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class Config:

    ROOT_PATH = os.path.abspath('.')

    LOG_PATH = ROOT_PATH + '/logs'

    APP_LOG_FILE = ROOT_PATH + '/logs/admin.log'

    SECRET_KEY = os.environ.get("SECRET_KEY") or "xd9\x85\x9c\xbc\x19\x9b\xe6ch\xdd\x12\x04F\x87%R5\xb3\xa7\xc2P\x93P\xe2"


class DevelopmentConfig(Config):
    DEBUG = True
    # 废弃
    SSO_SWITCH = False
    # SSO测试账号
    SSO_TEST_ACCOUNT = 'admin@youmi.net'
    # session lifetime
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    SESSION_COOKIE_NAME = "auth"
    SESSION_COOKIE_HTTPONLY = False
    SQLALCHEMY_DATABASE_URI = "mysql+cymysql://youmi:iloveUMLife123@172.16.1.50/youmi"
    SQLALCHEMY_BINDS = {
        # "youmi": SQLALCHEMY_DATABASE_URI,
        "admin": "mysql+cymysql://youmi:iloveUMLife123@172.16.1.50/youmi_admin",
        "spot": "mysql+cymysql://youmi:iloveUMLife123@172.16.1.50/youmi_spot",
        "stat": "mysql+cymysql://youmi:iloveUMLife123@172.16.1.50/youmi_stat",
        "data": "mysql+cymysql://youmi:iloveUMLife123@172.16.1.50/youmi_data",
        "rtb_report": "mysql+cymysql://youmi:iloveUMLife123@172.16.1.50/youmi_rtb_report",
        "rtb": "mysql+cymysql://youmi:iloveUMLife123@172.16.1.50/youmi_rtb"
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDSHIFT = "dbname=youmi_stats user=ymserver password=host=youmi-statsdata.cpwyku9ohxzt.cn-north-1.redshift.amazonaws.com.cn port=5439"
    AUDIENCE_REDSHIFT = "dbname=youmi_analyser user=ymserver password=host=youmi-statsdata.cpwyku9ohxzt.cn-north-1.redshift.amazonaws.com.cn port=5439"
    SENTRY_DSN = "http://29e17e66e54747d796a76d10d73d13d3:136a2735eba84f65af8461776eb3d197@sentry.awscn.umlife.net/20"
    RTB_LOG_01 = 'http://censor.y.cn'
    UPLOAD_FOLDED = '/home/liqifeng/YouMiCode/operate/tmp'


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass



config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}