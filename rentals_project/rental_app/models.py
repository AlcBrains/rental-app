from django.db import models

from .managers import ReservationManager
# Create your models here.


class Rental(models.Model):
    name = models.CharField(max_length=255)


class Reservation(models.Model):
    rental = models.ForeignKey(to=Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    objects = ReservationManager()
