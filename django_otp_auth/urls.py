from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
admin.site.register = "Rashid Otp"
admin.site.site_title = "Tutorial Learning"
admin.site.index_title = "Wisfrags Education"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls', namespace='account'))
]
