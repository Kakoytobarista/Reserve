from django.urls import path, include
from django.contrib.auth import views


urlpatterns = [
    path('', views.LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
]
