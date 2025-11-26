from django.db import models

# Create your models here.
class Floor(models.Model):
    storey = models.IntegerField()
    
class Zone(models.Model):
    length = models.DecimalField()
    width = models.DecimalField()
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

class BuildingElement(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    zone = models.ManyToManyField()

    class Meta:
        abstract = True

class Column(models.Model):
    geometry = models.CharField()

class Wall(models.Model):
    color = models.CharField()
