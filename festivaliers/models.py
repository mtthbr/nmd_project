from django.db import models
from datetime import datetime

# Create your models here.
class Festivalier(models.Model):
  first_name = models.CharField(max_length=128)
  email = models.EmailField()
  feedback = models.TextField(blank=True)
  sign_in_date = models.DateTimeField(default=datetime.now, blank=True)
  feedback_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.first_name