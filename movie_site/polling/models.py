from django.db import models
from django.db.models.aggregates import Count
from random import randint

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    total_likes = models.Count

    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def __str__(self):
        return self.title

class User(models.Model):
    ip_address = models.GenericIPAddressField()
    movies_polled = models.ManyToManyField(Movie)

    def __str__(self):
        return self.ip_address

