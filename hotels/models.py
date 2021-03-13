from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    description = models.TextField()
    no_of_rooms = models.IntegerField(default=0)
    email = models.EmailField()
    mobile = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)


    def __str__(self):
        return self.id 