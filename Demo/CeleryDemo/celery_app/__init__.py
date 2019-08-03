from celery import Celery, platforms

platforms.C_FORCE_ROOT = True
app = Celery('demo')
app.config_from_object('celery_app.config')

