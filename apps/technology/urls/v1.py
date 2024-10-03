from django.urls import path
from apps.technology.api_endpoints import technology, profession

urlpatterns = [
    path('',technology.TechnologyListCreateView.as_view(), name='technology'),
    path('profession/',profession.ProfessionListCreateView.as_view(), name='profession'),
]