from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from .forms import LoginForm
from .views import signup, profile, user_detail

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm),
        name='login'),
    path('password_change/',
         PasswordChangeView.as_view(template_name='users/password_change.html'),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/',
         PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    path('signup/', signup, name="signup"),
    path('edit/profile/', profile, name="profile"),
    path('user_detail/<int:user_id>', user_detail, name="user_detail"),
]
