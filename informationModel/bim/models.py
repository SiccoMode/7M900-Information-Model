from django.db import models
from django.utils.translation import gettext_lazy as _

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
    

    class ProgressState(models.TextChoices):
        READYFORCONSTRUCTION = "RE", _("Ready for Construction")
        UNDERCONSTRUCTION = "UC", _("Under Construction")
        COMPLETED = "CO", _("Completed")
        DELAYED = "DE", _("Delayed")
        PLANNED = "PL", _("Planned")

    current_state = models.CharField(choices=ProgressState)
    class Meta:
        abstract = True

class Column(models.Model):
    class GeometryType:
        CIRCULAR = "C"
        SQUARE = "SQ"
        RECTENGULAR = "RE"
    
    geometry = models.CharField(choices=GeometryType)

class Wall(models.Model):
    color = models.CharField()
