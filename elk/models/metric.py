from elk.libs.db.mysql import db

class Metric(object):
    _table = 'metric'

    def __init__(
            self, id_, name, es_index, es_path,
            unit, alert, created, updated):
        self.id_ = str(id_)
        self.name = name
        self.es_index = es_index
        self.es_path = es_path
        self.unit = unit
        self.alert = alert
        self.created = created
        self.updated = updated

    def dump(self):
        req = dict(
            id = self.id_,
            name = self.name,
            es_index = self.es_index,
            es_path = self.es_path,
            unit = self.unit,
            alert = self.alert,
            created = self.created,
            updated = self.updated)
        return req

    @classmethod
    def getAllList(cls):
        sql = ("select id as id_, name, es_index, es_path, "
                "unit, alert, created, updated "
                "from {table}").format(table=cls._table)
        rs = db.execute(sql).fetchall()
        db.commit()
        return [cls(*line) for line in rs] if rs else []
