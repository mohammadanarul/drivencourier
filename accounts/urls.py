from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    CustomerRegisterView,
    EmailVerifyView,
    PasswordResetView,
    EmailPasswordResetVerifyView,
    password_reset_confirmation_view,
    # users
    AccountListView,
    RiderRegisterView,
    ManagerRegisterView,
)

app_name = 'accounts'
urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer_register'),
    path('rider-register/', RiderRegisterView.as_view(), name='rider_register'),
    path('manager-register/', ManagerRegisterView.as_view(), name='manager_register'),
    path('verification/', EmailVerifyView.as_view(), name='verification_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset_view'),
    path('password-reset-otp-verify/', EmailPasswordResetVerifyView.as_view(), name='password_reset_otp_view'),
    path('password-reset-confirm/<otp>/', password_reset_confirmation_view, name='password_reset_confirm_view'),
    path('users/', AccountListView.as_view(), name='users_view'),
    # path('password-reset-confirm/<str:otp>/', EmailPasswordResetConformView.as_view(), name='password_reset_confirm_view'),
]