
from django.urls import path, include


from sprawdzian import quotes
urlpatterns = [
    path("", quotes.main, name="index"),
    path("<str:topic>/", quotes.get_tutorial),
    path("<str:topic>/<str:chapter>/", quotes.get_chapter),
]