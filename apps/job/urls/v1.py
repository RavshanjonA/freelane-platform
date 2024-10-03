from django.urls import path
from apps.job.api_endpoints import job_announce, job_location

urlpatterns = [
    path('job-announce/', job_announce.JobAnnounceListCreateView.as_view(), name="job"),
    path('job-announce/<id>/', job_announce.JobAnnounceRetrieveUpdateDestroyView.as_view(), name="job-detail"),
    path('job-location/', job_location.JobLocationListCreateView.as_view(), name="job-location")
]
