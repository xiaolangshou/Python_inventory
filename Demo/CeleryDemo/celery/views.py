from django.shortcuts import render
from celery import Celery, platforms

import time

broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379'
platforms.C_FORCE_ROOT = True

app = Celery(__file__, broker=broker, backend=backend)

# Create your views here.
@app.task
def add(x, y):
    time.sleep(5)
    return x + y

