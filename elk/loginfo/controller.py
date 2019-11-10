from elk.libs.es.elk import ELK
from elk.utils import logger
from elk.exception import EsError, EsNotFound   
from elk.config import ES_SERVER

logging = logger(__name__)

class Log(object):
    
    logtype_list = ['alertlog']
    
    @classmethod
    def find_by_condition(cls):
        es_index = "filebeat*"
        logtype = Log.logtype_list[0]
        data = []
        # query es
        try:
            es = ELK(es_index)
        except Exception as es:
            msg = "ES %s connection error." % ES_SERVER
            logging.error(msg)
            raise EsError(msg)
        logs_data = es.log_query()
        if logs_data:
            for logs in logs_data['hits']:
                source_data = logs['_source']
                data.append({"time": source_data['@timestamp'], "message": source_data['message'], "logtype": logtype})
        else:
            msg = "Not found index %s from es." % es_index
            logging.error(msg)
            raise EsNotFound(msg)
        return data
