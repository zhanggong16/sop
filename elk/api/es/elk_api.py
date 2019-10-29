from flask_restful import Resource, reqparse
from flask import request, jsonify
from elk.libs.es.elk import ELK
from elk.api.es.elk_controller import BaseApi
from elk.utils import logger, turn_cts_datetime

logging = logger(__name__)


class ELKApi(BaseApi):

    def __init__(self):
        super(ELKApi, self).__init__()

    def get(self):

        data = request.json
        logging.info("ELKApi get method start, param: %s." % data)
        need_fields = ('action',)
        self.check_keys(data, need_fields)
        self.check_values(data)
           
        action = data.get('action')
        metrics = data.get('metric')
        starttime = data.get('starttime')
        endtime = data.get('endtime')

        metrics_list = []
        for metric_dict in metrics:
            metric_info_from_db = self.check_metric(metric_dict)
            metric_dict.update(metric_info_from_db)
            metrics_list.append(metric_dict)

        if action == 'last_query':
            # call controller
            data_list = self._last_query(metrics_list)
            # return view   
            view_data = self._query_views(data_list)            
        elif action in ('range_query', 'groupby_query'):
            self.check_date_string('starttime', starttime)
            self.check_date_string('endtime', endtime)
            self.check_date_size(starttime, endtime)
       
            starttime = self.local_string_to_utc(starttime)
            endtime = self.local_string_to_utc(endtime)
            
            logging.info("ELKApi get method range_query param, starttime: %s, endtime: %s."
                            % (starttime, endtime))
            # call controller
            data_list = self._range_query(metrics_list, starttime, endtime)
            # return view   
            if action == 'range_query':
                view_data = self._query_views(data_list)
            elif action == 'groupby_query':
                groupby = 1
                view_data = self._query_views(data_list, groupby)
        return jsonify({'data': view_data, 'status': 200})
        
    def _last_query(self, metrics_list):
        '''
            input: 
                    metrics_list, [{u'name': u'library_hit.library_hit', 'es_path': u'library_hit', u'hostname': u'hytest', u'dbname': u'dsmdb', 'unit': u'%', 'es_index': u'library_hit'}, {u'name': u'library_hit.type', 'es_path': u'type', u'hostname': u'hytest', u'dbname': u'dsmdb', 'unit': u'null', 'es_index': u'library_hit'}]
        
            output: 
                    [
                    data_list, {u'name': u'library_hit.library_hit', 'es_path': u'library_hit', u'hostname': u'hytest', 'data': {u'hits': [{u'sort': [1567275480099], u'_type': u'_doc', u'_source': {u'@version': u'1', u'@timestamp': u'2019-08-31T18:18:00.099Z', u'hostname': u'hytest', u'library_hit': 99, u'type': u'library_hit_id', u'dbname': u'dsmdb'}, u'_score': None, u'_index': u'library_hit-7.2.0-2019.08.31', u'_id': u'WYLm6GwBPXZqCoylCCyq'}], u'total': {u'relation': u'eq', u'value': 5548}, u'max_score': None}, u'dbname': u'dsmdb', 'unit': u'%', 'es_index': u'library_hit'},
                    {u'name': u'library_hit.type', 'es_path': u'type', u'hostname': u'hytest', 'data': {u'hits': [{u'sort': [1567275480099], u'_type': u'_doc', u'_source': {u'@version': u'1', u'@timestamp': u'2019-08-31T18:18:00.099Z', u'hostname': u'hytest', u'library_hit': 99, u'type': u'library_hit_id', u'dbname': u'dsmdb'}, u'_score': None, u'_index': u'library_hit-7.2.0-2019.08.31', u'_id': u'WYLm6GwBPXZqCoylCCyq'}], u'total': {u'relation': u'eq', u'value': 5548}, u'max_score': None}, u'dbname': u'dsmdb', 'unit': u'null', 'es_index': u'library_hit'}
                    ]
        '''
        data_list = []
        for metrics in metrics_list:
            dbname = metrics.get('dbname')
            hostname = metrics.get('hostname')
            es_index = metrics.get('es_index') + '*'
            es = ELK(es_index)
            res = es.last_query(hostname, dbname)
            if not res:
                logging.warning("ELK _last_query index: %s not found in es." % es_index)
            metrics['data'] = res
            data_list.append(metrics)
        return data_list

    def _range_query(self, metrics_list, starttime, endtime):
        
        data_list = []
        for metrics in metrics_list: 
            dbname = metrics.get('dbname')
            hostname = metrics.get('hostname')
            es_index = metrics.get('es_index') + '*'
            es = ELK(es_index)
            res = es.range_query(starttime, endtime, hostname, dbname)
            if not res:
                logging.warning("ELK _range_query index: %s not found in es." % es_index)
            metrics['data'] = res
            data_list.append(metrics)
        return data_list


    def _query_views(self, data_list, groupby=0):
        '''
            {
                axis: ["mon", "thu", "wen", "thr", "fri", "sar", "sun"],
                data: [{
                        name: "CPU1",
                        value: [1, 2, 3, 4, 5, 6, 7]
                        }, {
                        name: "CPU2",
                        value: [1, 2, 3, 4, 5, 6, 7]
                        }]
            }

        '''
        res_list = []
        for metrics in data_list:
            if metrics['data']:
                time_list, v_data_list = [], []
                inner_data = metrics['data']['hits']
                for each_data in inner_data:
                    inner_each_data = each_data['_source']
                    time = inner_each_data['@timestamp']
                    time = turn_cts_datetime(time)
                    time_list.append(time)

                    for k in metrics['es_path'].split('.'):
                        inner_each_data = inner_each_data[k]
                    v_data_list.append(str(inner_each_data))
                v_data_dict = {
                                'name': str(metrics['name']), 
                                'value': v_data_list,
                                'unit': str(metrics['unit']),
                                'hostname': str(metrics['hostname']),
                                'dbname': str(metrics['dbname'])
                                }
                res_list.append(v_data_dict)
        time_list.reverse()
        res_list.reverse()
        
        if groupby:
            data_dict = dict()
            groupby_data_list = res_list[0]
            for i in groupby_data_list.get('value'):
                if i != 'None':
                    if i in data_dict:
                        data_dict[i] += 1
                    else:
                        data_dict[i] = 1
            g_data_list = []
            for k, v in data_dict.items():  
                g_data_list.append({'value': k, 'count': v})   
            groupby_data_list['value'] = g_data_list
            view_dict = {
                'data': [groupby_data_list],
                'total': len(time_list)
            }
        else:
            view_dict = {
                'axis': time_list,
                'data': res_list,
                'total': len(time_list)
            }
        return view_dict
