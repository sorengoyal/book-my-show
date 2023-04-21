from django.db import models
from django.utils.translation import gettext_lazy as _

from portal.models import Screen


class Seat(models.Model):
    class SeatType(models.TextChoices):
        VIP = "V", _("VIP")
        GOLD = "G", _("GOLD")
        SILVER = "S", _("SILVER")

    row = models.IntegerField()
    col = models.IntegerField()
    type = models.CharField(max_length=1, choices=SeatType.choices)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)

    def __str__(self):
        return "[%d] (%d,%d) %s" % (self.id, self.row, self.col, self.type)

