from elk.libs.db.mysql import db

class HostPool(object):
    _table = 'host_pool'

    def __init__(
            self, id_, uid, name, hostname, cpu_info, cpu_models, memory, 
            mount_info, ip_info, os_type, os_version, app_type, uptime, status, 
            deleted, deleted_at, created, updated):
        self.id_ = str(id_)
        self.uid = uid
        self.name = name
        self.hostname = hostname
        self.cpu_info = cpu_info
        self.cpu_models = cpu_models
        self.memory = memory
        self.mount_info = mount_info
        self.ip_info = ip_info
        self.os_type = os_type
        self.os_version = os_version
        self.app_type = app_type
        self.uptime = uptime
        self.status = status
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created = created
        self.updated = updated

    def dump(self):
        req = dict(
            id = self.id_,
            uid = self.uid,
            name = self.name,
            hostname = self.hostname,
            cpu_info = self.cpu_info,
            cpu_models = self.cpu_models,
            memory = self.memory,
            mount_info = self.mount_info,
            ip_info = self.ip_info,
            os_type = self.os_type,
            os_version = self.os_version,
            app_type = self.app_type,
            uptime = self.uptime,
            status = self.status,
            deleted = self.deleted,
            deleted_at = self.deleted_at,
            created = self.created,
            updated = self.updated)
        return req

    @classmethod
    def get_all_list(cls):
        sql = ("select id as id_, uid, name, hostname, cpu_info, cpu_models, memory, "
                "mount_info, ip_info, os_type, os_version, app_type, uptime, status, "
                "deleted, deleted_at, created, updated "
                "from {table} where deleted=0 order by created").format(table=cls._table)
        rs = db.execute(sql).fetchall()
        db.commit()
        return [cls(*line) for line in rs] if rs else []

    @classmethod
    def get_all_by_uid(cls, uid):
        sql = ("select id as id_, uid, name, hostname, cpu_info, cpu_models, memory, "
                "mount_info, ip_info, os_type, os_version, app_type, uptime, status, "
                "deleted, deleted_at, created, updated "
                "from {table} where uid=:uid and deleted=0").format(table=cls._table)
        params = {"uid": uid}
        rs = db.execute(sql, params=params).fetchall()
        db.commit()
        return [cls(*line) for line in rs] if rs else []
