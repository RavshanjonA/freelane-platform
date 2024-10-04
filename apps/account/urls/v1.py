from django.urls import path
from apps.account.api_endpoints import auth, activation, notification,account_detail

urlpatterns = [
    path('login/', auth.LoginView.as_view(), name="login"),
    path('register/', auth.RegisterView.as_view(), name="register"),
    path('notification/', notification.NotificationListView.as_view(), name="notifications"),
    path('notification/<pk>/', notification.NotificationRetrieveView.as_view(), name="notification"),
    path('send-code/', activation.SendActivationCodeView.as_view(), name="send-code"),
    path('verify-code/', activation.VerificationCodeView.as_view(), name="verify-code"),
    path('account-detail/<int:pk>/', account_detail.AccountRetrieveUpdateDestroyView.as_view(), name="account_detail"),
]
