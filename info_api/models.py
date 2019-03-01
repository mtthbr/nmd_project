from django.db import models


class Artiste(models.Model):
  nom = models.CharField(max_length = 70)
  pays = models.CharField(max_length = 70, blank=True)
  description = models.TextField(blank=True)
  path_photo = models.CharField(max_length = 300, blank=True)
  scene = models.CharField(max_length = 30)
  jour = models.CharField(max_length = 15)
  horaire_debut = models.DateTimeField(null=True)
  horaire_fin = models.DateTimeField(null=True)
  rs_link_1 = models.CharField(max_length = 450, blank=True)
  rs_link_2 = models.CharField(max_length = 450, blank=True)
  rs_link_3 = models.CharField(max_length = 450, blank=True)
  def __str__(self):
    return self.nom

class Course(models.Model):
  jour = models.CharField(max_length=15)
  type = models.CharField(max_length=25)
  heure_debut = models.DateTimeField(null=True)
  heure_fin = models.DateTimeField(null=True)
  description = models.TextField(blank=True)
  def __str__(self):
    return self.type

class Notification(models.Model):
  titre = models.CharField(max_length = 100)
  type = models.CharField(max_length=25)
  message = models.TextField()
  lien = models.TextField(blank=True, null=True)
  date_pop = models.DateField(null=True)
  def __str__(self):
    return self.titre

class Description(models.Model):
  sujet = models.TextField(max_length=100)
  page = models.TextField(max_length=30)
  message = models.TextField()
  def __str__(self):
    return self.sujet

