from django.db.models import Q

from config.celery import app


@app.task(bind=True, ignore_result=True)
def create_notification_for_developers(self, instance_id):
    from apps.account.models import AccountInfo, Notification
    from apps.account.choices import  NotificationType
    from apps.job.models import JobAnnounce
    instance = JobAnnounce.objects.get(id=instance_id)
    technology_ids = instance.technology.values_list("id", flat=True)
    developers = AccountInfo.objects.filter(
        Q(technologies__in=technology_ids) | Q(profession=instance.profession)
    ).distinct()
    notes = []
    for developer in developers:
        # Notification.objects.create()
        n = Notification(
            message=instance.title,
            type=NotificationType.JOB_ANNOUNCE,
            account=developer,
            url=instance.build_url
        )
        notes.append(n)
    Notification.objects.bulk_create(notes)
