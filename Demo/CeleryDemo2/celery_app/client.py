from celery_app import task1
from celery_app import task2

task1.add.delay(1, 2)
task2.say.delay()
