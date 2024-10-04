from django_filters import rest_framework

from apps.job.models import JobAnnounce
from apps.technology.models import Technology


class JobAnnounceFilter(rest_framework.FilterSet):
    city = rest_framework.CharFilter(field_name="location__city", lookup_expr='icontains')
    country = rest_framework.CharFilter(field_name="location__country", lookup_expr='icontains')
    level = rest_framework.CharFilter(field_name='level', lookup_expr='exact')
    technology = rest_framework.ModelMultipleChoiceFilter(
        field_name='technology__name',
        queryset=Technology.objects.all(),
        to_field_name='name'
    )
    price_measure = rest_framework.CharFilter(field_name='price_measure', lookup_expr='exact')
    payment_verified = rest_framework.CharFilter(field_name='payment_verified', lookup_expr='exact')
    job_type = rest_framework.CharFilter(field_name='job_type', lookup_expr='exact')
    profession = rest_framework.CharFilter(field_name='profession__name', lookup_expr='exact')
    price_from = rest_framework.CharFilter(field_name='price',lookup_expr='gte')
    price_to = rest_framework.CharFilter(field_name='price',lookup_expr='lte')
    class Meta:
        model = JobAnnounce
        fields = ['city',
                  'country',
                  'level',
                  'technology',
                  'price_measure',
                  'payment_verified',
                  'job_type',
                  'profession'
                  ]
