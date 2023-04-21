from django.db import models

from portal.models.city import City


class Theatre(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%d %s %s %s" % (self.id, self.name, self.address, self.city.name)

