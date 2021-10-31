from django.db import models


# Create your models here.
class Scoreboard(models.Model):
    username = models.CharField(max_length=10)
    score = models.IntegerField(default=0)
    date = models.DateField()


