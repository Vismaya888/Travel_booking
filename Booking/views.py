from django.shortcuts import render, redirect,get_object_or_404
from .models import Destination,Flight,Booking

# Create your views here.
def index(request):
    flight_set = Flight.objects.all()
    return render(request,'index.html',{'data':flight_set})
def about(request):
    flight_set = Flight.objects.all()
    return render(request,'about.html',{'data':flight_set})
def blog(request):
    return render(request,'blog.html')
def contact(request):
    flight_set = Flight.objects.all()
    return render(request,'contact.html',{'data':flight_set})
def destination(request):
    return render(request,'destination.html')
def guide(request):
    return render(request,'guide.html')
def package(request):
    return render(request,'package.html')
def service(request):
    flight_set = Flight.objects.all()
    return render(request,'service.html',{'data':flight_set})
def single(request):
    return render(request,'single.html')
def testimonial(request):
    return render(request,'testimonial.html')
def destination_list(request):
    data_set = Destination.objects.all()
    return render(request,'listing.html',{'data':data_set})
def flight_list(request):
    flight_set = Flight.objects.all()
    return render(request,'flights.html',{'data':flight_set})

from .forms import BookingForm

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.total_price = calculate_total_price(booking)
            booking.booking_reference = generate_booking_reference()
             
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})


def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'booking_confirmation.html', {'booking': booking})


from django.contrib import messages
from .models import Booking  # Import your Booking model

def cancel_booking(request, booking_id):
    # Retrieve the booking using the ID
    booking = get_object_or_404(Booking, id=booking_id)

    # Check if the request method is POST to confirm the cancellation
    if request.method == 'POST':
        # Perform cancellation logic
        booking.status = 'Cancelled'  # Update the status of the booking
        booking.save()
        
        messages.success(request, 'Your booking has been successfully cancelled.')
        return redirect('booking_cancellation_success')  # Redirect to a success page
    
    # If GET request, render a confirmation template
    return render(request, 'confirm_cancellation.html', {'booking': booking})


from decimal import Decimal

def calculate_total_price(booking):
    # Assume flight and hotel prices are Decimal fields
    total_price = Decimal('0.00')

    # Add flight price if a flight is selected
    if booking.flight:
        total_price += booking.flight.price

    # Add additional charges, if any
    # (Add more calculation logic here as needed)

    return total_price

from django.utils.crypto import get_random_string


def generate_booking_reference():
    while True:
        reference = get_random_string(length=12).upper()  # Generates a 12-character alphanumeric string
        if not Booking.objects.filter(booking_reference=reference).exists():
            return reference

def booking_cancellation_success(request):
    return render(request,'booking_cancellation_success.html')


def Booking_list(request):
    booking_set = Booking.objects.all()
    return render(request,'myBookings.html',{'data':booking_set})

# def delete_booking(request, booking_id):
#     # Retrieve the booking using the ID
#     booking = get_object_or_404(Booking, id=booking_id)

#     # Check if the request method is POST to confirm the deletion
#     if request.method == 'POST':
#         booking.delete()  # Delete the booking record from the database
#         messages.success(request, 'Your booking has been successfully deleted.')
#         return redirect('canclled')  # Redirect to a success page
    
#     # If GET request, render a confirmation template
#     return render(request, 'myBookings.html', {'booking': booking})


def cancelled_booking(request):
    return render(request,'cancelled.html')

def delete_list(request,pk):
    instance = Booking.objects.get(pk=pk)
    instance.delete()
    data = Booking.objects.all()
    return render(request,'myBookings.html',{'data':data})
    