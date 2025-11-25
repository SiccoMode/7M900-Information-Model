from django.db import models

# Create your models here.
class Floor(models.Model):
    storey = models.IntegerField()
    