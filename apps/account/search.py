from django_filters import rest_framework

from apps.account.models import Notification


class NotificationListFilter(rest_framework.FilterSet):
    type = rest_framework.CharFilter(field_name='type', lookup_expr='exact')
    is_read = rest_framework.BooleanFilter(field_name='is_read', lookup_expr='exact')

    class Meta:
        model = Notification
        fields = ['type', 'is_read']
