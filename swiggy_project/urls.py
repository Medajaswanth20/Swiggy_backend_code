# swiggy_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swiggy/', include('swiggy_app.urls')),  # Add this line to include your app's URLs
]
