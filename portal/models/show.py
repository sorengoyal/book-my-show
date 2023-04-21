from django.db import models

from portal.models.movie import Movie
from portal.models.screen import Screen
from portal.models.seat import Seat


class Show(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    screen = models.ForeignKey(Screen, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return "[%d] '%s' '%s' '%s' '%s'" % (self.id, self.movie.name, self.screen.name, self.start_time, self.end_time)





