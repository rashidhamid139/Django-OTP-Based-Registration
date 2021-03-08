from django.urls import path
from . import views
app_name = 'register'

urlpatterns = [
    path('register-phone/<str:reset>/', views.registerpages, name='register-phone'),
    path('', views.homepage, name='homepage'),
    path('validate_otp/<str:reset_to_password>/', views.validateOTP, name='validate-otp'),
    path('register_user', views.registerUser, name='register-user'),
    path('password_reset/<str:phone>/', views.passwordReset, name='password-reset'),
]


