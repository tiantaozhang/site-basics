class YMException(Exception):
    """
    Api exceptions
    代替 werkzeug.exceptions
    """
    code = None
    message = None
    sentry_alarm = True
    logging = True

    def __init__(self, message=None, sentry_alarm=None, logging=None):
        """
        :param message: string, error message
        :param sentry_alarm: boolean, 是否通过sentry报警
        :param logging: boolean, 是否记录日志
        """
        if message is not None:
            self.message = message
        if sentry_alarm is not None:
            self.sentry_alarm = sentry_alarm
        if logging is not None:
            self.logging = logging


class BadRequest(YMException):
    """http请求url或者参数错误"""
    code = 400


class InternalServerError(YMException):
    """http请求内部错误"""
    code = 500


class AuthSSORequired(YMException):
    """sso required"""
    code = 210
    sentry_alarm = False
    logging = False


class AuthInvalidAccount(YMException):
    """无效账号"""
    code = 220
    sentry_alarm = False
    logging = False


class AuthSignatureError(YMException):
    """无效签名"""
    code = 240
    sentry_alarm = False
    logging = False


class AuthPermissionDeny(YMException):
    """权限错误,无权限访问"""
    code = 240
    sentry_alarm = False
    logging = False
