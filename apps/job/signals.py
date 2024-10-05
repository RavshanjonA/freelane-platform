from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.job.models import JobAnnounce
from apps.job.tasks import create_notification_for_developers


# @receiver(post_save, sender=JobAnnounce)
# def create_notification_signal(sender, instance: JobAnnounce, created, **kwargs):
#     if created:
#         create_notification_for_developers.delay(instance_id=instance.id)
