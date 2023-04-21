from django.db import models
from django.utils.translation import gettext_lazy as _
from portal.models.theatre import Theatre


class Screen(models.Model):
    class Feature(models.IntegerChoices):
        NONE = 0
        THREE_D_PROJECTOR = 1
        DOLBY_SOUND = 2

    MAX_HEIGHT = 100
    MAX_WIDTH = 100

    name = models.CharField(max_length=100)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    feature = models.IntegerField(choices=Feature.choices, blank=True)

    def __str__(self):
        return "[%d] '%s' '%s' '%s'" % (self.id, self.name, self.theatre.name, self.feature)
