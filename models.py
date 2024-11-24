
from django.db import models

class Game(models.Model):
    word = models.CharField(max_length=100)
    guesses = models.TextField()
    max_attempts = models.IntegerField(default=6)

