# encoding: utf-8
from flask import request
from elk.api.es.elk_api import ELKApi


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

header = ""

api_router = [
    {
    'resource_name': ELKApi,
    'name': 'ELKApi',
    'url': '/v1.0/elk',
    'desc': '查询metric接口',
    },
]

