import django_filters

from apps.account.models import Notification


class NotificationFilterBackend(django_filters.Filter):
    class Meta:
        model = Notification
        fields = {'type': ['exact'], 'is_read': ['exact']}
