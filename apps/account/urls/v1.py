from django.urls import path
from apps.account.api_endpoints import auth, activation
urlpatterns = [
    path('login/', auth.LoginView.as_view() ),
    path('register/', auth.RegisterView.as_view() ),
    path('send-code/', activation.SendActivationCodeView.as_view()),
    path('verify-code/', activation.VerificationCodeView.as_view()),
]