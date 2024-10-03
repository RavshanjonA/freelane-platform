from rest_framework.generics import ListCreateAPIView

from apps.technology.api_endpoints.technology.TechnologyListCreate.serializers import TechnologyListCreateSerializer
from apps.technology.models import Technology


class TechnologyListCreateView(ListCreateAPIView):
    queryset = Technology.objects.filter(is_verified=True)
    serializer_class = TechnologyListCreateSerializer


__all__ = ("TechnologyListCreateView",)
