from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.contrib import messages  # Import messages module for error messages
from .models import Event, Booking, Company, CompanyCategory
from .forms import ClientRegistrationForm, CompanyRegistrationForm




def index(request):
    categories = CompanyCategory.objects.all()
    return render(request, 'index.html', {'categories': categories})


def category(request, category_id):
    category = CompanyCategory.objects.filter(pk=category_id).first()
    companies = Company.objects.filter(category=category)
    return render(request, 'company_list.html', {'companies': companies})

def events(request, company_id):
    company = Company.objects.get(pk=company_id)
    events = Event.objects.filter(owner=company)
    return render(request, 'events_list.html', {'events': events, 'company': company})

@login_required
def event_registration(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        booking = Booking.objects.create(
            client = request.user.client,
            event = event
        )
        return redirect('profile')
    return render(request, 'event_registration.html', {'event': event})

def booking_success(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return render(request, 'booking_success.html', {'booking': booking})


def client_registration(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the appropriate URL
    else:
        form = ClientRegistrationForm()
    return render(request, 'client_registration.html', {'form': form})

def company_registration(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the appropriate URL
    else:
        form = CompanyRegistrationForm()
    return render(request, 'company_registration.html', {'form': form})



class CustomLoginView(View):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect on successful login
        else:
            message = "Invalid credentials"
            messages.error(request, message)  # Display error message

        return render(request, self.template_name, {'message': message})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
def CustomLogout(request):
    logout(request)
    return HttpResponse("Loggged out")


def profile(request):
    user = request.user.client
    booking = Booking.objects.filter(client=user)
    return render(request, 'profile.html', {'booking': booking })