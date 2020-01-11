from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from envcfg.json.elk import ES_SERVER

class ELK(object):
    
    def __init__(self, index):
        self.elk_host_array = ES_SERVER.split(",")
        self.client = Elasticsearch(hosts=self.elk_host_array, timeout=10)
        self.index = index
        self.search_client = Search(using=self.client, index=self.index)        
        #self.max_range_size = 86400 / 60 * 7
        self.max_range_size = 8000

    def range_query(self, starttime, endtime, hostname, dbname):
        query_search = self.search_client.filter('range', **{'@timestamp': {'gte': starttime, 'lte': endtime}})
        if hostname:
            query_search = query_search.filter("term", hostname=hostname.lower())
        if dbname:
            query_search = query_search.filter("term", dbname=dbname.lower())
        query_search = query_search.sort({"@timestamp": {"order": "desc"}})
        query_search = query_search[0:self.max_range_size]
        try:
            response = query_search.execute()
        except NotFoundError:
            return None
        else:
            return response.to_dict()['hits']

    def sql_ash_query(self, starttime, endtime, opt=None):
        query_search = self.search_client
        query_search = self.search_client.filter('range', **{'@timestamp': {'gte': starttime, 'lte': endtime}})
        if opt:
            query_search = query_search.query({"term": {"machine": opt.lower()}})
        query_search = query_search.sort({"@timestamp": {"order": "asc"}})
        query_search = query_search[0:self.max_range_size]
        try:
            response = query_search.execute()
        except NotFoundError:
            return None
        else:
            return response.to_dict()['hits']

    def metric_range_query(self, starttime, endtime, metricset=None, hostname=None, name=None):
        query_search = self.search_client
        query_search = self.search_client.filter('range', **{'@timestamp': {'gte': starttime, 'lte': endtime}})
        if metricset:
            query_search = query_search.query({"term": {"metricset.name": metricset.lower()}})
        if hostname:
            query_search = query_search.query({"term": {"host.hostname": hostname.lower()}})
        if metricset == "network":
            if name:
                query_search = query_search.query({"term": {"system.network.name": name.lower()}})
        query_search = query_search.sort({"@timestamp": {"order": "asc"}})
        query_search = query_search[0:self.max_range_size]
        try:
            response = query_search.execute()
        except NotFoundError:
            return None
        else:
            return response.to_dict()['hits']

    def metric_last_query(self, metricset_list=None, hostname=None):
        query_search = self.search_client
        if metricset_list:
            query_search = query_search.query({"terms": {"metricset.name": metricset_list}})
        if hostname:
            query_search = query_search.query({"term": {"host.hostname": hostname.lower()}})
        query_search = query_search.sort({"@timestamp": {"order": "desc"}})
        query_search = query_search[0:1]
        try:
            response = query_search.execute()
        except NotFoundError:
            return None
        else:
            return response.to_dict()['hits']

    def log_query(self):
        query_search = self.search_client
        query_search = query_search.sort({"@timestamp": {"order": "desc"}})
        #query_search = query_search[0:100]
        try:
            response = query_search.execute()
        except NotFoundError:
            return None
        else:
            return response.to_dict()['hits']
