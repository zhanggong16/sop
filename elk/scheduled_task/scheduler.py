from .task import *

SCHEDULER_API_ENABLED = True
JOBS = [
    {
        'id': 'test_task',
        'func': test_task,
        'args': '',
        'trigger': 'interval',
        'seconds': 3600
    },
]
