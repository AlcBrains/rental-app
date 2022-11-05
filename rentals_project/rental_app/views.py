from django.views.generic import ListView

from .models import Reservation


class ReservationList(ListView):
    model = Reservation
    template_name = "reservations.html"
