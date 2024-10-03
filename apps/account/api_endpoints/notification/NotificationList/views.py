from rest_framework.generics import ListAPIView

from apps.account.api_endpoints.notification.NotificationList.serializers import NotificationListSerializer
from apps.account.models import Notification


class NotificationListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationListSerializer

    def get_queryset(self):
        return self.queryset.filter(account=self.request.user.accountinfo)


__all__ = ("NotificationListView",)
