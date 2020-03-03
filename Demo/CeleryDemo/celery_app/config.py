BROKER_URL = 'redis://192.168.1.232:6379'
CELERY_RESULT_BACKEND = 'redis://192.168.1.232:6379/0'

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)

