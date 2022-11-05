from django.db import models
from django.db.models import OuterRef, Subquery


class ReservationManager(models.Manager):

    def get_raw_data_eager(self):
        return super().get_queryset().prefetch_related('rental')

    def get_queryset(self):
        return self.get_raw_data_eager().annotate(prev_res_id=Subquery(self.with_prev_reservation_id()))

    def with_prev_reservation_id(self):
        # select r.id, r.checkin, r.checkout, ren.name,
        # (select res.id from rental_app_reservation res where res.checkin < r.checkin and res.rental_id = r.rental_id order by checkin desc)
        # from rental_app_reservation r join rental_app_rental ren on r.rental_id = ren.id;
        return self.get_raw_data_eager().filter(rental=OuterRef("rental"), checkin__lt=OuterRef("checkin")).order_by("-checkin").values("pk")
