from django.db import models

# Create your models here.
from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class DonationRecord(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    orphanage_name = models.CharField(max_length=255)
    # This stores the items as a dictionary: {"Soap": 2, "Toothbrush": 1}
    items_donated = models.JSONField() 
    occasion = models.CharField(max_length=100)
    occasion_details = models.TextField(null=True, blank=True)
    delivery_mode = models.CharField(max_length=50) # Pickup or Drop-off
    pickup_address = models.TextField(null=True, blank=True) # Only filled if Pickup
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.name} -> {self.orphanage_name}"