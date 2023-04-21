from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%d %s" % (self.id, self.name)

