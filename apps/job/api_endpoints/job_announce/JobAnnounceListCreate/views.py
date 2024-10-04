from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView

from apps.job.api_endpoints.job_announce.JobAnnounceListCreate.serializers import JobAnnounceListCreateSerializer
from apps.job.models import JobAnnounce
from apps.job.search import JobAnnounceFilter


class JobAnnounceListCreateView(ListCreateAPIView):
    queryset = JobAnnounce.objects.all()
    serializer_class = JobAnnounceListCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = JobAnnounceFilter
    search_fields = ['title', 'body']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


__all__ = ("JobAnnounceListCreateView",)
