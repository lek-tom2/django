
from django.contrib import admin
from django.urls import path, include

from sprawdzian import quotes
urlpatterns = [
    path("", quotes.main, name="index"),
    path("<str:author>", quotes.get_author, name="author"),
]