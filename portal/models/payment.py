from django.db import models

# Create your models here.
class Payment(models.Model):
    price = models.FloatField()
    external_ref_id = models.IntegerField(default=0)

    def __str__(self):
        return "[%d] $%d %d" % (self.id, self.price, self.external_ref_id)
