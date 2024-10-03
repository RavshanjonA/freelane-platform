from rest_framework.generics import ListCreateAPIView

from apps.job.api_endpoints.job_announce.JobAnnounceListCreate.serializers import JobAnnounceListCreateSerializer
from apps.job.models import JobAnnounce


class JobAnnounceListCreateView(ListCreateAPIView):
    queryset = JobAnnounce.objects.all()
    serializer_class = JobAnnounceListCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


__all__ = ("JobAnnounceListCreateView",)
