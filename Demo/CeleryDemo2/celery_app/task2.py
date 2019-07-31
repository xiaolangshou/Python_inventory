from celery_app import app
import time


@app.task
def say():
    time.sleep(2)
    return 'hello'


