from force.db.store import DistributedSQLStore, init_context
from envcfg.json.elk import MYSQL_DSN

master_ctx = init_context('elk', dsn=MYSQL_DSN)
slave_ctxes = []
db = DistributedSQLStore.init_by_context(master_ctx, slave_ctxes)
