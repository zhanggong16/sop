#!/usr/bin/env python
from elasticsearch_dsl import Search, A
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

import pytz
import datetime
from tzlocal import get_localzone


ES_SERVER = '172.31.23.21:9200'

class ELK(object):
    
    def __init__(self):
        self.elk_host_array = ES_SERVER.split(",")
        self.client = Elasticsearch(hosts=self.elk_host_array, timeout=60)
        self.index = 'sql_ash*'
        self.search_client = Search(using=self.client, index=self.index)        

    def last_query(self):
        hostname = 'elkserver'
        starttime = local_string_to_utc('2019-11-26 12:00:00')
        endtime = local_string_to_utc('2019-11-26 13:00:00')
        
        query_search = self.search_client
        query_search = self.search_client.filter('range', **{'@timestamp': {'gte': starttime, 'lte': endtime}})
        #query_search = query_search.query({"term": {"machine": "hytest"}})
        #query_search = query_search.filter("term", name=hostname.lower())
        #query_search = query_search.query({"match": {"metricset.name": "diskio"}})
        #query_search = query_search.query({"terms": {"metricset.name": ["filesystem",]}})
        #query_search = query_search.query({"term": {"host.name": "hytest"}})
        #query_search = query_search.query({"term": {"system.network.name": "lo"}})
        #query_search = query_search.sort({"@timestamp": {"order": "desc"}})
        query_search = query_search[0:1000]
        
        try:
            response = query_search.execute()
        except NotFoundError:
            return None
        else:
            return response.to_dict()['hits']['hits']


def local_string_to_utc(time_string, time_format='%Y-%m-%d %H:%M:%S'):
    try:
        local_dt = datetime.datetime.strptime(time_string, time_format)
        local_tz = get_localzone()
        localize_dt = local_tz.localize(local_dt)
        return localize_dt.astimezone(pytz.UTC)
    except ValueError:
        raise ValueError   


a = ELK()
res = a.last_query()
for i in res:
    #print i.get('_source').get("system").get("network").get("out").get("bytes")
    print i
#for i in a.last_query():
#    res = i['_source']
#    print res['@timestamp'], res['event']
    #if res['system']:
    #    if res['system'].get('process'):
    #        print res['@timestamp'], res['system'].get('process').get('memory')
            
    

