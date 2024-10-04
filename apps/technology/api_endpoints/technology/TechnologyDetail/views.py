from rest_framework import generics

from apps.technology.api_endpoints.technology.TechnologyDetail.serializers import TechnologyRetrieveUpdateSerializer
from apps.technology.models import Technology


class TechnologyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologyRetrieveUpdateSerializer

__all__ = ('TechnologyRetrieveUpdateDestroyView',)