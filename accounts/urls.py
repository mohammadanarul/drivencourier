from django.urls import path
from accounts.views import marchent, rider, auth, password_reset, user

app_name = 'accounts'


urlpatterns = [
    path('register/', marchent.MarchentRegisterView.as_view(), name='customer_register'),
    path('rider-register/', rider.RiderRegisterView.as_view(), name='rider_register'),
    # auth urls
    path('login/', auth.LoginView.as_view(), name='login_view'),
    path('logout/', auth.LogoutView.as_view(), name='logout_view'),
    path('verification/', password_reset.EmailVerifyView.as_view(), name='verification_view'),
    # user urls
    path('users/', user.AccountListView.as_view(), name='user_list_view'),
    path('add-user/', user.AccountCreateView.as_view(), name='user_create_view'),
    path('update-user/<pk>/', user.AccountUpdateView.as_view(), name='user_update_view'),
    path('delete-user/<pk>', user.AccountDeleteView.as_view(), name='user_delete_view'),
    # password reset urls
    path('password-reset/', password_reset.PasswordResetView.as_view(),
         name='password_reset_view'),
    path('otp-verify/', password_reset.EmailPasswordResetVerifyView.as_view(),
         name='password_reset_otp_view'),
    path('password-reset-confirm/<otp>/', password_reset.password_reset_confirmation_view,
         name='password_reset_confirm_view'),
]
