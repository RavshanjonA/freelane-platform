from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status


from apps.account.api_endpoints.notification.NotificationList.serializers import NotificationListSerializer
from apps.account.filters import NotificationFilterBackend
from apps.account.models import Notification


class NotificationListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationListSerializer
    filterset_class = NotificationFilterBackend

    def get_queryset(self):
        return self.queryset.filter(account=self.request.user.accountinfo)

    @action(detail=False, methods=['POST'], url_path='mark_as_read_notifications')
    def mark_all_as_read(self, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.filter(is_read=False).update(is_read=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


__all__ = ("NotificationListView",)
