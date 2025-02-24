from celery import Celery
from core.config import settings
import time

celery_app = Celery('worker', broker=settings.CELERY_BROKER_URL,backend=settings.CELERY_BACKEND_URL)

celery_app.conf.update(    
    broker_connection_retry_on_startup=True,  # Add this line to avoid the warning
)

@celery_app.task
def add_number(x,y):
    time.sleep(10)
    return x+y