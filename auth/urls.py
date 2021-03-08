from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from register.views import loginUser as UserLogin, resetPassword
admin.site.site_header = "USER Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls', namespace='account')),
    path('register/', include('register.urls', namespace='register')),
    path("login/", UserLogin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('forgot_password', resetPassword, name='forgot-password'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)