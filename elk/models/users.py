from elk.libs.db.mysql import db

class Users(object):
    _table = 'users'

    def __init__(
            self, id_, name, passwd, email, role, 
            alert, deleted, created, updated):
        self.id_ = str(id_)
        self.name = name
        self.passwd = passwd
        self.email = email
        self.role = role
        self.alert = alert
        self.deleted = deleted
        self.created = created
        self.updated = updated
 
    def dump(self):
        req = dict(
            id = self.id_,
            name = self.name,
            passwd = self.passwd,
            email = self.email,
            role = self.role,
            alert = self.alert,
            deleted = self.deleted,
            created = self.created,
            updated = self.updated)
        return req

    @classmethod
    def list(cls):
        sql = ("select id as id_, name, passwd, email, role, "
                "alert, deleted, created, updated "
                "from {table}").format(table=cls._table)
        rs = db.execute(sql).fetchall()
        db.commit()
        return [cls(*line) for line in rs] if rs else []
   
    @classmethod
    def get_passwd_by_name(cls, name):
        sql = ("select id, name, passwd, role from "
                "{table} where name=:name and deleted=0").format(table=cls._table)
        params = dict(name = name)
        rs = db.execute(sql, params=params).fetchone()
        db.commit()
        return rs if rs else ''

    @classmethod
    def get_id_by_name(cls, name):
        sql = ("select id from "
                "{table} where name=:name").format(table=cls._table)
        params = dict(name = name)
        rs = db.execute(sql, params=params).fetchone()
        db.commit()
        return rs if rs else ''

    @classmethod
    def get_name_by_id(cls, id):
        sql = ("select id, name, passwd, role from "
                "{table} where id=:id and deleted=0").format(table=cls._table)
        params = dict(id = id)
        rs = db.execute(sql, params=params).fetchone()
        db.commit()
        return rs if rs else ''

    @classmethod
    def add(cls, insert_dict):
        mysql_table = cls._table
        sql = ('insert into {table} '
               '(name, passwd, email, role, alert, deleted) '
               'values (:name, :passwd, :email, :role, :alert, :deleted) '
               ).format(table=mysql_table)
        params = insert_dict
        id_ = db.execute(sql, params=params).lastrowid
        if not id_:
            db.rollback()
            return
        db.commit()
        return str(id_)

    @classmethod
    def update(cls, update_dict):
        mysql_table = cls._table
        sql = ('update {table} set name=:name, passwd=:passwd, '
               'email=:email, alert=:alert, deleted=:deleted '
               'where id=:id').format(table=mysql_table)
        params = update_dict
        db.execute(sql, params=params).lastrowid
        db.commit()
        return

    @classmethod
    def delete(cls, delete_id):
        sql = 'delete from {table} where id=:id_'.format(
            table=cls._table)
        params = dict(id_=delete_id)
        db.execute(sql, params)
        db.commit()
        return delete_id
