from rest_framework import generics

from apps.account.api_endpoints.auth.Register.serializers import RegisterSerializer
from apps.account.models import Account


class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer


__all__ = ("RegisterView",)
