from rest_framework import serializers

from apps.account.models import Notification


class NotificationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("id", "message", "is_read", "type", "url")
