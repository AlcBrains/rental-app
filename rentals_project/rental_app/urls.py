from django.conf import settings
from django.urls import path, include
from rental_app import views



urlpatterns = [
    path('', views.ReservationsList.as_view(), name='base'),
]

