from elk.models.host_pool import HostPool
from elk.utils import logger

logging = logger(__name__)

class Database(object):

    @classmethod
    def all_list(cls):
        rs = HostPool.get_all_list()
        return [line.dump() for line in rs]

    @classmethod
    def format_data(cls, data_dict):
        '''
            input dict
            Formatted database instance list details
        '''
        data = dict()
        for k, v in data_dict.items():
            if k == "mount_info":
                data['mount_info'] = [i.replace(",", " ") for i in v.split("|")]
            elif k == "ip_info":
                data['ip_info'] = v.split("|")
            else:
                data[k] = v
        return data

    @classmethod
    def detail_data(cls, uid):
        '''
            return one dict
        '''
        if uid:
            rs = HostPool.get_all_by_uid(uid)
            return cls.format_data([line.dump() for line in rs][0])
        else:
            return 
