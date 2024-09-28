from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenViewBase

from apps.account.api_endpoints.auth.Login.serializers import LoginSerializer


class LoginView(TokenViewBase):
    serializer_class = LoginSerializer


__all__ = ("LoginView",)
