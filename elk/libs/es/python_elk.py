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
        self.index = 'sql_ash-*'
        self.search_client = Search(using=self.client, index=self.index)        

    def last_query(self):
        #starttime = local_string_to_utc('2019-08-26 20:05:00')
        #endtime = local_string_to_utc('2019-08-26 20:09:00')
        
        #query_search = self.search_client.filter('range', **{'@timestamp': {'gte': starttime, 'lte': endtime}})
        #a = A('terms', field='event')
        #query_search = query_search.aggs.bucket('event', a)
        #query_search = query_search.aggs.metric('zhg', 'terms', field='event')
        
        query_search = query_search.sort({"@timestamp": {"order": "desc"}})
        query_search = query_search[0:1]
        
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
#print a.last_query()

for i in a.last_query():
    res = i['_source']
    print res['@timestamp'], res['event']
    #if res['system']:
    #    if res['system'].get('process'):
    #        print res['@timestamp'], res['system'].get('process').get('memory')
            
    

