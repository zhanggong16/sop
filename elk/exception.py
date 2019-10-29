# encoding: utf-8
from collections import namedtuple

Error = namedtuple('Error', ['code', 'message', 'http_status_code'])


class ElkError(Exception):
    """Elk Base Exception."""
    _error = Error(0, '未知错误', 400)

    def __init__(self, message=''):
        super(ElkError, self).__init__(message)
        self.message = message or self._error.message
        self.code = self._error.code
        self.http_status_code = self._error.http_status_code


#: 基础类错误(1 ~ 99)
class DatabaseOperationError(ElkError):
    _error = Error(1, 'Failed to update the metadata', 402)

class MissParametersError(ElkError):
    _error = Error(11, 'Miss parameters', 400)

class CheckMetricError(ElkError):
    _error = Error(12, 'Check metric not support', 400)

class ParametersValueError(ElkError):
    _error = Error(13, 'Parameters value not support', 400)

class ApiAuthError(ElkError):
    _error = Error(14, 'Api auth error', 400)
