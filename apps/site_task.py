import sys
sys.path.append('../')

from celery import Celery
from config.celery_setting import BROKER_URL


app = Celery('tasks', broker=BROKER_URL)


@app.task
def add(x, y):
    return x + y
