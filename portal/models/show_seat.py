from django.db import models

from portal.models.seat import Seat
from portal.models.show import Show


class ShowSeat(models.Model):
    class Status(models.IntegerChoices):
        AVAILABLE = 1
        BOOKED = 2
        ON_HOLD = 3

    show = models.ForeignKey(Show, on_delete=models.DO_NOTHING)
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    status = models.IntegerField(choices=Status.choices)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        status_str = self.Status(self.status).name
        return "[%d] %d (%d,%d) %s $%d" % (self.id, self.show.id, self.seat.row,self.seat.col, status_str, self.price)


