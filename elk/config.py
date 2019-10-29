from envcfg.json.elk import HTTP_PORT
from envcfg.json.elk import DEBUG
from envcfg.json.elk import ES_SERVER


APP = 'elk'
LOG_FILE = '/var/log/{}.log'.format(APP)
METRIC_XML = '/opt/elk/elk/api/elk_target.xml'

AUTH_PASSWD = 'Hcloud321'

__all__ = [
    'HTTP_PORT',
    'DEBUG',
    'LOG_FILE',
    'ES_SERVER',
    'METRIC_XML'
]
