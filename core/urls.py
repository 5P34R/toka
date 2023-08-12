from django.urls import path

from .views import CustomLogout, index, event_registration, booking_success, events, client_registration, company_registration, CustomLoginView, category, profile

urlpatterns = [
    path('', index, name='home'),
    path('company/<int:company_id>/events/', events, name='events'),
    path('category/<int:category_id>/register/', category, name="category"),
    path('event/<int:event_id>/register/', event_registration, name='event_registration'),
    path('booking/<int:booking_id>/success/', booking_success, name='booking_success'),
    path('client-registration/', client_registration, name="client_registration"),
    path('company-registration/', company_registration, name="company_registration"),
    path('profile/', profile, name="profile"),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogout, name='logout')    
    
]