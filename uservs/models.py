from django.db import models
from datetime import datetime

# Create your models here.
class Uservs(models.Model):
  prenom = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  feedback = models.TextField(blank=True)
  date_inscription = models.DateTimeField(default=datetime.now, blank=True)
  date_feedback = models.DateTimeField(blank=True, null=True)
  def __str__(self):
    return self.prenom