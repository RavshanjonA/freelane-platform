from django.urls import path
from apps.technology.api_endpoints import technology, profession

urlpatterns = [
    path('',technology.TechnologyListCreateView.as_view(), name='technology'),
    path('<int:pk>/', technology.TechnologyRetrieveUpdateDestroyView.as_view(), name='technology-detail'),
    path('profession/',profession.ProfessionListCreateView.as_view(), name='profession'),
    path('profession/<int:pk>/',profession.ProfessionRetrieveUpdateDestroy.as_view(), name='profession-detail'),
]