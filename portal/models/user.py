from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    class Role(models.TextChoices):
        CUSTOMER = "CU", _("Customer")

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.CUSTOMER)

    def __str__(self):
        return "%d %s %s %s" % (self.id, self.name, self.email, self.role)



