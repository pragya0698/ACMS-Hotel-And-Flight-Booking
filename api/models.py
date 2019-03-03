from django.db import models
import uuid
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Hotel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular hotel')
    
    name = models.CharField(max_length=100)

#    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
   
    city_name = models.ForeignKey(City, on_delete=models.CASCADE) 

    address = models.CharField(max_length=200)

    checkintime = models.TimeField()

    extratime = models.DurationField()
    #extra time is for the hotel to clean(used to calculate checkout time)

    image_link = models.CharField(max_length=500, default="")

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this hotel."""
        return reverse('hotel-detail', args=[str(self.id)])

class RoomType(models.Model):
    #use this to allow the hotels to add new types of rooms
    name = models.CharField(max_length=200, help_text='Enter type of room')
    def __str__(self):
        """String for representing the Model object."""
        return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.core.validators import MinValueValidator, MaxValueValidator

class HotelRoom(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular hotel')
    
    roomno = models.CharField(max_length=6, default='A000')
    
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, null=True)

    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    description = models.TextField(max_length=1000, help_text='Enter description of the room.')

    price = models.DecimalField(max_digits=6, decimal_places=2)

    category = models.ForeignKey('RoomType', on_delete=models.SET_NULL, null=True)#use when hotels can add new types of rooms

    """
    #use when hotels can't add new types of room
    RoomType = (
        ('nor', 'Normal(Non-AC)'),
        ('ac', 'AC'),
        ('del', 'Delux'),
    )

    category = models.CharField(
        max_length=3,
        choices=RoomType,
        default='nor',
        help_text='Room Type',
    )
    """

#    class Meta:
#        ordering = ['price']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.roomno} ({self.hotel.name})'

from django.utils import timezone
class RoomAvailability(models.Model):
    room = models.ForeignKey('HotelRoom', on_delete=models.CASCADE, null=True)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
#    class Meta:
#        odering = ['date']

    def __str__(self):
        """String for representing the Model object."""
        return f'({self.room.roomno})({self.room.hotel.name})'
