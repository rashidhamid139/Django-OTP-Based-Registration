from django.urls import path
from . import views
from knox import views as knox_views

app_name = 'account'

urlpatterns = [
    path('validate_phone/', views.ValidatePhoneSendOTP.as_view(), name='validate-phone'),
    path('validate_otp', views.ValidateOTP.as_view(), name='validate-otp'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]
