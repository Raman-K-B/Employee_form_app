from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')),  # replace 'employees' with your app folder name
    path('', RedirectView.as_view(url='/employees/list/', permanent=True)),  # Redirect root URL to employee list
]
