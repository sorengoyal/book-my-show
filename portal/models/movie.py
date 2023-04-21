from django.db import models


class Movie(models.Model):

    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    length = models.IntegerField()

    def __str__(self):
        return '[%d] %s %s %s' % (self.id, self.name, self.director, self. length)
