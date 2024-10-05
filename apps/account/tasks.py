import random
from datetime import datetime, timedelta

from celery import shared_task
from django.core.cache import cache
from django.db.models import Q

from apps.account.choices import NotificationType
from config.celery import app


@app.task(bind=True, ignore_result=True)
def send_activation_code(self, phone):
    code = random.randint(1000, 9999)
    cache.set(phone, code, 240)
    print(code)
    with open("code.txt", "w") as f:
        f.write(str(code))


@shared_task
def delete_old_notifications():
    from apps.account.models import Notification
    Notification.objects.filter(Q(is_read=True) & Q(updated_at__lte=datetime.now() - timedelta(days=1))).delete()


@shared_task
def mark_read_last_week_notification():
    from apps.account.models import Notification
    Notification.objects.filter(Q(is_read=False) & Q(created_at__gte=datetime.now() - timedelta(days=7)))


