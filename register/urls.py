from django.urls import path
from . import views
app_name = 'register'

urlpatterns = [
    path('register-phone/', views.registerpages, name='register-phone'),
    path('', views.homepage, name='homepage'),
    path('validate_otp/', views.validateOTP, name='validate-otp'),
    path('register_user', views.registerUser, name='register-user'),
    path('password_reset/', views.passwordReset, name='password-reset'),
    #ajaxreset
    path('reset_pass_ajax/', views.resetPasswordAjax, name='ajax-reset-password'),

]


