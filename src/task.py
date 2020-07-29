from celery import Celery
from os import system
from celery.schedules import crontab

app = Celery(
    'task',
    broker = 'redis://redis:6379/0',
    backend = 'redis://redis:6379/0'
)


@app.task
def check():
    cmd = "python3 manage.py check_date"
    return system(cmd)

@app.task
def add_holidays():
    cmd = 'python3 manage.py add_holidays'
    return system(cmd)

app.conf.beat_schedule = {
    'task': {
        'task': 'task.check',
        'schedule': crontab(minutes=0, hour=1),
    }
}

app.conf.beat_schedule = {
    'task':{
        'task':'task.add_holidays',
        'schedule':crontab(0, 0, day_of_month='1'),
    }
}