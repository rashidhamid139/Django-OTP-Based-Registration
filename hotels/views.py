from django.shortcuts import render, get_object_or_404
from .models import Hotel, Room

# Create your views here.
def allHotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})


def hotelDetail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel })