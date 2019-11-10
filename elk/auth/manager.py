from elk.models.users import Users
from elk.utils import logger
from elk.extension import login_manager

logging = logger(__name__)


class User():
    def __init__(self, username, id, role, active=True):
        self.username = username
        self.id = id
        self.active = active
        self.role = role

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_annonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def get_role(self):
        return self.role

    def __repr__(self):
        return '<User %r>' % (self.id)


@login_manager.user_loader
def load_user(id):
    rs = Users.get_name_by_id(id)
    uid, name, passwd, role = rs
    return User(name, id, role)

def do_auth(username, password):
    rs = Users.get_passwd_by_name(username)
    if not rs:
        logging.error("do_auth: failed, username %s does not exist." % username)
        return
    try:
        uid, name, passwd, role = rs
    except Exception as e:
        logging.error("do_auth: failed, error %s." % e)
        return 
    if password == str(passwd):
        logging.info("do_auth: username %s auth success, role %s." % (username, role))
        return [uid, role]
    else:
        logging.info("do_auth: username %s password %s auth failed." % (username, password)) 
        return   
