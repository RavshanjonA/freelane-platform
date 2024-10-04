from rest_framework import generics

from apps.technology.api_endpoints.profession.ProfessionRetrieveUpdateDestroy.serializers import \
    ProfessionRetrieveUpdateSerializer
from apps.technology.models import Profession


class ProfessionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionRetrieveUpdateSerializer


__all__ = ('ProfessionRetrieveUpdateDestroy',)
