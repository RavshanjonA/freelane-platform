from rest_framework.generics import ListCreateAPIView

from apps.technology.api_endpoints.profession.ProfessionListCreate.serializers import ProfessionListCreateSerializer
from apps.technology.models import Profession
from apps.technology.search import TrigramSearchFilter


class ProfessionListCreateView(ListCreateAPIView):
    queryset = Profession.objects.filter(is_verified=True)
    serializer_class = ProfessionListCreateSerializer
    filter_backends = [TrigramSearchFilter]


__all__ = ("ProfessionListCreateView",)
