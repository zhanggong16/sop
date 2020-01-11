# encoding: utf-8
from elk.libs.es.elk import ELK
from elk.utils import logger, local_string_to_utc, grouper
from elk.exception import EsError, EsNotFound   
from elk.models.host_pool import HostPool
import time

logging = logger(__name__)

class Monitor(object):
    
    def __init__(self):
        pass

    @classmethod
    def all_list(cls):

        map_const = {"running": "success", "failed": "warning"}

        def _map(data_dict):
            for k, v in data_dict.items():
                if k == 'status':
                    data_dict["status_label"] = map_const.get(v, 'danger')
            return data_dict

        rs = HostPool.get_all_list()
        return [_map(line.dump()) for line in rs]

class Performance(Monitor):
    
    @classmethod
    def _get_sqlash(cls, starttime, endtime, opt):
        # opt ~ machine
        #if opt == "sop_default":
        opt = "hytest"
        es_index = "sql_ash*"
        try:
            es = ELK(es_index)
        except Exception as ex:
            logging.error("Performance _get_sqlash, init ES error: %s." % ex)
            return {}
        starttime = local_string_to_utc(starttime)
        endtime = local_string_to_utc(endtime)
        res = es.sql_ash_query(starttime, endtime, opt)
        return res

    @classmethod
    def one_sqlash_graph_data(cls, resp):
        starttime = "2019-11-27 12:00:00"
        endtime = "2019-11-27 13:00:00"
        res = Performance._get_sqlash(starttime, endtime, opt)
        
    

    @classmethod
    def wait_class(cls, opt):
        name = "count"
        starttime = "2019-11-26 10:00:00"
        endtime = "2019-11-26 13:00:00"
        res = Performance._get_sqlash(starttime, endtime, opt)
        if res.get("hits"):
            data_dict = dict()
            data_list = []
            for item in res.get("hits"):
                data = item.get("_source").get("wait_class")
                logging.info("yyy %s" % item)
                # data = "System I/O, Concurrency"
                if not data:
                    break
                #for data in data_ora.split(','):
                if data in data_dict:
                    data_dict[data] += 1
                else:
                    data_dict[data] = 1
            logging.info("xxx %s" % data_dict)
            for k, v in data_dict.items():
                data_list.append([str(k), int(v)])
            return {"name": name, "data": [["System I/O", 3], ["Concurrency", 4]]}
        else:
            logging.warning("Performance, get data %s, empty?" % res)
            return {"name": name, "data": []}
        
    

class HostMonitor(Monitor):
    
    title_display = [
                        {'fid': 1, 'unit': '空', 'name': '负载LOAD', 'metricset': 'load'},
                        {'fid': 2, 'unit': '%', 'name': 'CPU使用率', 'metricset': 'cpu'},
                        {'fid': 3, 'unit': '%', 'name': '内存使用率', 'metricset': 'memory'},
                        {'fid': 4, 'unit': 'KB', 'name': '网络流量', 'metricset': 'network'},
                        {'fid': 5, 'unit': 'KB', 'name': '硬盘性能', 'metricset': 'diskio'},
                    ]
    # 86400 / 10 / 2 half day
    max_display_item = 4000  


    def __init__(self):
        super(HostMonitor, self).__init__()

    @classmethod
    def get_title_display(cls):
        title_display = [
                        {'fid': 1, 'unit': '空', 'name': '负载LOAD', 'metricset': 'load'},
                        {'fid': 2, 'unit': '%', 'name': 'CPU使用率', 'metricset': 'cpu'},
                        {'fid': 3, 'unit': '%', 'name': '内存使用率', 'metricset': 'memory'},
                        {'fid': 4, 'unit': 'KB', 'name': '网络流量', 'metricset': 'network'},
                    ]
        return title_display

    @classmethod
    def _single_drill(cls, data, drill_key):
        res_format = ''
        time_array = time.strptime(data.get("@timestamp"), "%Y-%m-%dT%H:%M:%S.%fZ")
        time_stamp = int(time.mktime(time_array)) * 1000 + 8 * 3600 * 1000
        if drill_key == "load":
            #from process
            res = data.get("system").get("load")
            res_format = "%s, %s, %s" % (res.get("1"), res.get("5"), res.get("15"))
        elif drill_key ==  "memory":
            #from memory
            mem_used = int(data.get("system").get("memory").get("total")) - int(data.get("system").get("memory").get("free"))
            mem_total = int(data.get("system").get("memory").get("total"))
            res_format = "%.2f" % (float(mem_used) / float(mem_total) * 100)

        elif drill_key == "load 1min":
            result = data.get("system").get("load").get("1")
        elif drill_key == "load 5min":
            result = data.get("system").get("load").get("5")
        elif drill_key == "load 15min":
            result = data.get("system").get("load").get("15")
        elif drill_key == "mem_pct":
            mem_used = int(data.get("system").get("memory").get("total")) - int(data.get("system").get("memory").get("free"))
            mem_total = int(data.get("system").get("memory").get("total"))
            result = "%.2f" % (float(mem_used) / float(mem_total) * 100)
        elif drill_key == "cpu_total_pct":
            result = "%.2f" % (float(data.get("system").get("cpu").get("total").get("pct")) / data.get("system").get("cpu").get("cores"))
        elif drill_key == "in":
            result = "%.2f" % (data.get("system").get("network").get("in").get("bytes") / 1024)
        elif drill_key == "out":
            result = "%.2f" % (data.get("system").get("network").get("out").get("bytes") / 1024)
        elif drill_key == "read":
            result = "%.2f" % (data.get("system").get("diskio").get("read").get("bytes") / 1024)
        elif drill_key == "write":
            result = "%.2f" % (data.get("system").get("diskio").get("write").get("bytes") / 1024)
        if res_format:
            return res_format
        else:
            return [time_stamp, float(result)] 

    @classmethod
    def host_all_list(cls):
        es_index = "metricbeat*"
        try:
            es = ELK(es_index) 
        except Exception as ex:
            logging.error("HostMonitor, init ES error: %s." % ex)
            return Monitor.all_list()    
        
        res_all_list = []
        for host in Monitor.all_list():
            hostname = host.get('hostname')
            metricset = ["load"]
            process_res = es.metric_last_query(metricset, hostname)
            process_info = process_res.get('hits')[0].get('_source')
            if process_info:
                last_load = HostMonitor._single_drill(process_info, 'load')
            else:
                last_load = "0, 0, 0"
            metricset = ["memory"]
            process_res = es.metric_last_query(metricset, hostname)
            process_info = process_res.get('hits')[0].get('_source')
            if process_info:
                last_memory_pct = HostMonitor._single_drill(process_info, 'memory')
            else:
                last_memory_pct = 0.0
            host["last_load"] = last_load
            host["last_memory_pct"] = last_memory_pct
            res_all_list.append(host)
        return res_all_list
    
    ################## for monitor display
    @classmethod
    def get_title_list(cls):
        constant_display = {'interval': 60, 'aggregation': 'last'}
        title_display = HostMonitor.get_title_display()
        res_title_display = []
        for i in title_display:
            i.update(constant_display)
            res_title_display.append(i)
        return res_title_display

    @classmethod
    def _aggregate_item(cls, item_list):
        max_display_item = cls.max_display_item
        if len(item_list) > max_display_item:
            res_list = []
            step = len(item_list) / max_display_item + 3
            for g in grouper(item_list, step):
                time_stamp = g[-1][0]
                s = 0
                for d in g:
                    s += d[1]
                if isinstance(s, float):
                    data = float('%.2f' %  (s / len(g)))
                else:
                    data = s / len(g)
                res_list.append([time_stamp, data])
            return res_list
        else:
            return item_list

    @classmethod
    def _diff_list(cls, data_list):
        up_list = data_list[1:]
        down_list = data_list[:-1]
        res_list = []
        for i in range(len(up_list)):
            res_list.append([down_list[i][0], (up_list[i][1] - down_list[i][1])])
        return res_list

    @classmethod
    def get_monitor_json_data(cls, hostname, starttime, endtime):
        '''
            return [
                        {'res': [{"name": 123, "data": [[1573975800000.0, 1], [1573975900000.0, 2]]}], 'fid': 1},
                        {'res': [{"name": 123, "data": [[1573975800000.0, 1], [1573975900000.0, 2]]}, 
                                    {"name": 123, "data": [[1573975900000.0, 3], [1573975900000.0, 4]]}], 'fid': 2}
                    ]
        '''
        res_data_list = []
        title_display = HostMonitor.get_title_display()
        es_index = "metricbeat*"
        try:
            es = ELK(es_index)
        except Exception as ex:
            logging.error("HostMonitor, init ES error: %s." % ex)
            return []
        starttime = local_string_to_utc(starttime)
        endtime = local_string_to_utc(endtime)
        for item in title_display:
            sub_res_list = []
            metricset = item.get("metricset")
            try:
                if metricset == "load":
                    metric_res_info = es.metric_range_query(starttime, endtime, metricset, hostname)
                    load1_name, load2_name, load3_name = "load 1min", "load 5min", "load 15min"
                    load1_data, load2_data, load3_data = [], [], []
                    for source_data in metric_res_info.get("hits"):
                        data = source_data.get("_source")
                        load1_data.append(HostMonitor._single_drill(data, load1_name))
                        load2_data.append(HostMonitor._single_drill(data, load2_name))
                        load3_data.append(HostMonitor._single_drill(data, load3_name))
                    sub_res_list = [{"name": load1_name, "data": HostMonitor._aggregate_item(load1_data)},
                                    {"name": load2_name, "data": HostMonitor._aggregate_item(load2_data)},
                                    {"name": load3_name, "data": HostMonitor._aggregate_item(load3_data)},
                                    ]
                    res_data = {
                        "fid": item.get("fid"),
                        "res": sub_res_list
                        }
                elif metricset == "memory":
                    metric_res_info = es.metric_range_query(starttime, endtime, metricset, hostname)
                    total_name = "mem_pct"
                    total_data = []
                    for source_data in metric_res_info.get("hits"):
                        data = source_data.get("_source")
                        total_data.append(HostMonitor._single_drill(data, total_name))
                    sub_res_list = [{"name": total_name, "data": HostMonitor._aggregate_item(total_data)},
                                    ]
                    res_data = {
                        "fid": item.get("fid"),
                        "res": sub_res_list
                        }
                elif metricset == "cpu":
                    metric_res_info = es.metric_range_query(starttime, endtime, metricset, hostname)
                    total_name = "cpu_total_pct"
                    total_data = []
                    for source_data in metric_res_info.get("hits"):
                        data = source_data.get("_source")
                        total_data.append(HostMonitor._single_drill(data, total_name))
                    sub_res_list = [{"name": total_name, "data": HostMonitor._aggregate_item(total_data)},
                                    ]
                    res_data = {
                        "fid": item.get("fid"),
                        "res": sub_res_list
                        }
                elif metricset == "network":
                    filter_name = ["eth0"]
                    in_name, out_name = "in", "out"
                    sub_res_list = []
                    for f_name in filter_name:
                        in_data, out_data = [], []
                        metric_res_info = es.metric_range_query(starttime, endtime, metricset, hostname, f_name)
                        for source_data in metric_res_info.get("hits"):
                            data = source_data.get("_source")
                            in_data.append(HostMonitor._single_drill(data, in_name))
                            out_data.append(HostMonitor._single_drill(data, out_name))
                        in_data = HostMonitor._diff_list(in_data)
                        out_data = HostMonitor._diff_list(out_data)
                        in_res_list = [{"name": in_name + "-" + f_name, "data": HostMonitor._aggregate_item(in_data)},
                                        {"name": out_name + "-" + f_name, "data": HostMonitor._aggregate_item(out_data)},
                                        ]
                        sub_res_list += in_res_list
                    res_data = {
                        "fid": item.get("fid"),
                        "res": sub_res_list
                        }
                elif metricset == "diskio":
                    filter_name = [""]
                    metric_res_info = es.metric_range_query(starttime, endtime, metricset, hostname)
                    read_name, wirte_name = "read", "write"
                    read_data, wirte_data = [], []
                    for source_data in metric_res_info.get("hits"):
                        data = source_data.get("_source")
                        read_data.append(HostMonitor._single_drill(data, read_name))
                        wirte_data.append(HostMonitor._single_drill(data, wirte_name))
                    sub_res_list = [{"name": read_name, "data": HostMonitor._aggregate_item(read_data)},
                                    {"name": wirte_name, "data": HostMonitor._aggregate_item(wirte_data)},
                                    ]
                    res_data = {
                        "fid": item.get("fid"),
                        "res": sub_res_list
                        }
            except Exception as ex:
                logging.error("ES get data error, hostname: %s, metricset: %s, starttime: %s, endtime: %s. error: %s." 
                            % (hostname, metricset, starttime, endtime, ex))
                res_data = []
            res_data_list.append(res_data)
        #logging.info("xxx %s" % res_data_list)
        return res_data_list
