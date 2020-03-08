from django.db import models

# Create your models here.

class bookingmodel(models.Model):
    name = models.TextField(default="")
    start = models.DateTimeField(default="2000-01-01 00:00:00")
    end = models.DateTimeField(default="2000-01-01 00:00:00")