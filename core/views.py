from django.shortcuts import render, redirect
from .models import Event, Booking, Company
from .forms import EventRegistrationForm


def index(request):
    companies = Company.objects.all()
    return render(request, 'index.html', {'companies': companies})


def events(request, company_id):
    company = Company.objects.get(pk=company_id)
    events = Event.objects.filter(owner=company)
    return render(request, 'events_list.html', {'events': events, 'company': company})

def event_registration(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            booking = Booking.objects.create(client=client, event=event)
            return redirect('booking_success', booking_id=booking.id)
    else:
        form = EventRegistrationForm()
    return render(request, 'event_registration.html', {'form': form, 'event': event})

def booking_success(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return render(request, 'booking_success.html', {'booking': booking})
