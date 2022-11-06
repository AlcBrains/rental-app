from django.views.generic import ListView

from .models import Reservation


class ReservationsList(ListView):
    model = Reservation
    template_name = "reservations.html"
