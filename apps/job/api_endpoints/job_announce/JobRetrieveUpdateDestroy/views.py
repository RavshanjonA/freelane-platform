from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.job.api_endpoints.job_announce.JobRetrieveUpdateDestroy.serializers import \
    JobAnnounceRetrieveUpdateDestroySerializer
from apps.job.models import JobAnnounce


class JobAnnounceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = JobAnnounce.objects.all()
    serializer_class = JobAnnounceRetrieveUpdateDestroySerializer


__all__ = ("JobAnnounceRetrieveUpdateDestroyView",)
