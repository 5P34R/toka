from django.urls import path

from .views import index, event_registration, booking_success, events

urlpatterns = [
    path('', index, name='index'),
    path('company/<int:company_id>/events/', events, name='events'),
    path('event/<int:event_id>/register/', event_registration, name='event_registration'),
    path('booking/<int:booking_id>/success/', booking_success, name='booking_success'),    
]