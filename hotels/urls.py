from django.urls import path
from . import views
app_name= 'hotels'

urlpatterns = [
    path('', views.allHotels, name='hotels-list'),
    path('<int:pk>/', views.hotelDetail, name='hotel-detail')
]
