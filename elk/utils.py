#-*- coding:utf-8 -*-
from elk.config import LOG_FILE
import logging, os, subprocess
import time, datetime
import itertools
from xml.dom.minidom import parse

def logger(name):
    format='%(asctime)s [%(filename)s][%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.INFO, filename=LOG_FILE, filemode='a', format=format)
    logger = logging.getLogger(name)
    return logger


def run(cmd):
    _pipe = subprocess.PIPE
    obj = subprocess.Popen(cmd, stdin=_pipe,
                           stdout=_pipe,
                           stderr=_pipe,
                           env=os.environ,
                           shell=True)
    result = obj.communicate()
    obj.stdin.close()
    _returncode = obj.returncode
    return _returncode, result


def grouper(iterable, n):
    '''
    group a iterable into chunk
    i = [1, 2, 3, 4, 5]
    grouper(i, 2) => [[1, 2], [3, 4], [5]]
    '''
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

def timestamp_to_format(timestamp=None, format = '%Y-%m-%d %H:%M:%S'):
    # try:
    if timestamp:
        timestamp = float(timestamp)
        time_tuple = time.localtime(timestamp)
        res = time.strftime(format, time_tuple)
    else:
        res = time.strftime(format)
    return res

def turn_cts_datetime(datetime_utc):
    date_ = datetime.datetime.strptime(datetime_utc, "%Y-%m-%dT%H:%M:%S.%fZ")
    local_time = date_ + datetime.timedelta(hours=8)
    return local_time

def xml_key(doc):
    if os.path.isfile(doc):
        doc = parse(doc)
        metric_dict = {}
        for item in doc.getElementsByTagName("metric"):
            rank = item.getElementsByTagName('item')
            i = 0
            for node in rank:
                metric_dict[node.getAttribute("name")] = [node.childNodes[0].data, 
                            item.getElementsByTagName('unit')[i].childNodes[0].data]
                i += 1
        return metric_dict
    else:
        return
