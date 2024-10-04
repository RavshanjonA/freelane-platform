from rest_framework import generics

from apps.account.api_endpoints.account_detail.AccountDetail.serializers import AccountDetailSerializer
from apps.account.models import Account


class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer

__all__ = ('AccountRetrieveUpdateDestroyView',)