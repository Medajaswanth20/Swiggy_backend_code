from django.db import models
from django.contrib.auth.models import User

class Milestone(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
