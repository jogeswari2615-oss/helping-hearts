from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Donor, DonationRecord
from django.shortcuts import render

# Add this function to your existing views.py
def home(request):
    return render(request, 'index.html') # Make sure your HTML file is named index.html

@api_view(['POST'])
def submit_everything(request):
    data = request.data
    
    # 1. Save or Get the Donor (Login info)
    donor, created = Donor.objects.get_or_create(
        email=data['email'],
        defaults={
            'name': data['name'],
            'address': data['address'],
            'phone': data['phone'],
            'age': data.get('age'),
            'gender': data.get('gender')
        }
    )

    # 2. Save the Donation Details
    donation = DonationRecord.objects.create(
        donor=donor,
        orphanage_name=data['orphanage_name'],
        items_donated=data['items'], # This is your array of selected items
        occasion=data['occasion'],
        occasion_details=data['occasion_details'],
        delivery_mode=data['delivery_mode'],
        pickup_address=data['pickup_address']
    )

    return Response({"status": "success", "message": "Data stored in MySQL"})