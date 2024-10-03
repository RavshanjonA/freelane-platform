from rest_framework.generics import ListCreateAPIView

from apps.technology.api_endpoints.profession.ProfessionListCreate.serializers import ProfessionListCreateSerializer
from apps.technology.models import Profession


class ProfessionListCreateView(ListCreateAPIView):
    queryset = Profession.objects.filter(is_verified=True)
    serializer_class = ProfessionListCreateSerializer


__all__ = ("ProfessionListCreateView",)
