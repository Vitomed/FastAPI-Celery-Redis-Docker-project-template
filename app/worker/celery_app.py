from celery import Celery

from app.worker import celeryconfig

celery = Celery('worker')
celery.config_from_object(celeryconfig)
