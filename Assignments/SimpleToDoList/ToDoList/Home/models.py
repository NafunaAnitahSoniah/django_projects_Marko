from django.db import models
from django.utils import timezone

# Create your models here.
class Tasklist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duedate = models.DateField()
    priority = models.CharField(max_length=15)
    status = models.CharField(max_length=15)
    creationdate = models.DateTimeField(default=timezone.now)
