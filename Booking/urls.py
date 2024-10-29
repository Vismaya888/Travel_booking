from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('destination/',views.destination,name='destination'),
    path('guide/',views.guide,name='guide'),
    path('package/',views.package,name='package'),
    path('service/',views.service,name='service'),
    path('single/',views.single,name='single'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('list/destination/',views.destination_list,name='destination_list'),
    path('list/flight/',views.flight_list,name='flight_list'),
    path('list/book/',views.Booking_list,name='booking_list'),
    path('book/', views.create_booking, name='create_booking'),
    path('confirm/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    # path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('cancelled/',views.cancelled_booking,name='cancelled'),
    path('delete/<pk>',views.delete_list,name='delete'),

    # path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    # path('cancellation-success/', views.booking_cancellation_success, name='booking_cancellation_success'),
]
