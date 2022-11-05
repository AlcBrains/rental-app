from django.conf import settings
from django.urls import path, include
from rental_app import views



urlpatterns = [
    path('', views.ReservationList.as_view(), name='base'),
]

