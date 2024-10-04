from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.api_endpoints.notification.NotificationList.serializers import NotificationListSerializer
from apps.account.models import Notification
from apps.account.search import NotificationListFilter


class NotificationListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NotificationListFilter

    def get_queryset(self):
        return self.queryset.filter(account=self.request.user.account_info)


class MarkAsReadAPIView(APIView):
    def post(self, request):
        notifications = Notification.objects.filter(is_read=False, account=request.user.account_info)

        for notification in notifications:
            notification.is_read = True

        Notification.objects.bulk_update(notifications, ['is_read'])

        return Response({"message": "Notifications marked as read"}, status=200)


__all__ = ("NotificationListView","MarkAsReadAPIView")
