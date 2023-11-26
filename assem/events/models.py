from django.db import models
from django.contrib.auth.models import AbstractUser

class Event(models.Model):
    title = models.CharField(max_length=15)
    start = models.DateField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
#  // end: '{{ event.end|date:"c" }}',
