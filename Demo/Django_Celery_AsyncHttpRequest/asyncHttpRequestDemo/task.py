import os
import sys
import time
from django.conf import settings

app = settings.CELERY


@app.task
def f1():
    time.sleep(10)
    print('hello!')
    return "hello return！"
