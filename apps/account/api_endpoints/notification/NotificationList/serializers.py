from rest_framework import serializers

from apps.account.models import Notification


class NotificationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("id", "message", "type", "is_read")
