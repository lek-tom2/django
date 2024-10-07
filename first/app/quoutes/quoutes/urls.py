

from django.contrib import admin
from django.urls import path, include

from sprawdzian import quotes
urlpatterns = [
    path('admin/', admin.site.urls),
    path("quotes/", include("sprawdzian.urls"))
]
