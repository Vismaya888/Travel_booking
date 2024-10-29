from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Destination(models.Model):
    # Basic information
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    # Additional details
    climate = models.CharField(max_length=50, blank=True, null=True)
    best_time_to_visit = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)

    # Attractions and activities
    popular_attractions = models.TextField(help_text="List of popular attractions", blank=True, null=True)
    recommended_activities = models.TextField(help_text="List of recommended activities", blank=True, null=True)

    # Image and media (optional)
    image = models.ImageField(upload_to="destinations/", blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.country}"
    

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=50)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.IntegerField()
    def __str__(self):
        return f"{self.airline}, {self.flight_number}"

    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True, blank=True)
    
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    booking_reference = models.CharField(max_length=12, unique=True,null=True) 
    

    def __str__(self):
        return f"Booking {self.booking_reference} for {self.user.username} at {self.destination.name}"