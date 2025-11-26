from django.contrib import admin
from django.urls import path, include     # <-- Make sure BOTH are here!
from django.http import HttpResponse      # <-- Needed for the 'home' view

def home(request):
    return HttpResponse("Welcome to the Employee Project!")

urlpatterns = [
    path('', home, name='home'),  # This will show a welcome message at /
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
]
