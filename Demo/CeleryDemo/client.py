from celery_app import task1
from celery_app import task2

if __name__ == '__main__':
    task1.add.delay(1, 2)
    task2.say.delay()
