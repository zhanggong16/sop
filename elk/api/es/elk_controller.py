from flask_restful import Resource, reqparse
from flask import request
from elk.utils import logger, xml_key
from elk.config import METRIC_XML, AUTH_PASSWD
from elk.models.metric import Metric
from elk.exception import (
    MissParametersError, 
    CheckMetricError,
    ParametersValueError,
    ApiAuthError
)
import time
import pytz
import datetime
from tzlocal import get_localzone

logging = logger(__name__)

class BaseApi(Resource):
    '''
        action: [last_query, range_query]
        metric: 
        hostname:
        dbname: 
        starttime:
        endtime:
    '''
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('X-Password', location='headers')
        self.data = self.parser.parse_args()
        #if self.data.get('X-Password') != AUTH_PASSWD:
        #    msg = 'Request auth failed'
        #    logging.error(msg)
        #    raise ApiAuthError(msg)

######################################################################

    def check_keys(self, json_body, keys):
        for key in keys:
            if json_body.get(key) is None or json_body.get(key) == '':
                msg = 'key {key} should not be empty'.format(key=key)
                logging.error(msg)
                raise MissParametersError(msg)

    def check_values(self, json_body):

        check_dict = {
                'action': ['last_query', 'range_query', 'log_query', 'groupby_query'],    
        }

        for k, v in check_dict.items():
            value = json_body.get(k)
            if value:
                if value not in v:
                    msg = 'key metric vaule {va} not support, must be {d}'.format(va=value, d=v)
                    logging.error(msg)
                    raise ParametersValueError(msg)

    def check_date_string(self, key, date):
        try:
            time.strptime(date, "%Y-%m-%d %H:%M:%S")
        except:
            msg = '{k} vaule {v} error, ex: \'2019-08-17 14:00:00\''.format(k=key, v=date)
            logging.error(msg)
            raise ParametersValueError(msg)

    def check_date_size(self, starttime, endtime):
        if starttime > endtime: 
            msg = 'starttime {start} > endtime {end}, error'.format(start=starttime, end=endtime)
            logging.error(msg)
            raise ParametersValueError(msg)           

    def local_string_to_utc(self, time_string, time_format='%Y-%m-%d %H:%M:%S'):
        try:
            local_dt = datetime.datetime.strptime(time_string, time_format)
            local_tz = get_localzone()
            localize_dt = local_tz.localize(local_dt)
            return localize_dt.astimezone(pytz.UTC)
        except ValueError:
            msg = 'time_string {v} ValueError'.format(v=time_string)
            logging.error(msg)
            raise ParametersValueError(msg)
    
    def get_metric_info(self):
        rs = Metric.getAllList()
        return [line.dump() for line in rs]

    def check_metric(self, input_metric):
        ''' 
            input_metric, {'hostname': 'hytest', 'name': 'library_hit.library_hit', 'dbname': 'dsmdb'}
        '''       
        metric_list = self.get_metric_info()
        for metric_dict in metric_list:
            metric = "%s.%s" % (metric_dict.get('es_index'), metric_dict.get('name'))
            if metric == input_metric.get('name'):
                return {'es_path': metric_dict.get('es_path'),
                        'es_index': metric_dict.get('es_index'),
                        'unit': metric_dict.get('unit')
                        }
        msg = 'Metric {m} not support'.format(m=metric)
        logging.error(msg)
        raise CheckMetricError(msg)
        
    



 
