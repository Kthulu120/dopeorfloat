from __future__ import unicode_literals
from random import randint
from django.db import models
from django.db.models import Count


class Grabber(models.Model):
    imageLink = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    isRep = models.BooleanField(default=False)

    def getTwo(self):
        random = randint(0, Grabber.objects.all())
        return random

    def publish(self):
        self.save()

    def __str__(self):
        return self.imageLink

    def addVote(self):
        self.votes += 1
        self.save()
