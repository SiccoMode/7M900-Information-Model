import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Floor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    storey = models.IntegerField()
    
class Zone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    length = models.DecimalField()
    width = models.DecimalField()
    x = models.DecimalField()
    y = models.DecimalField()
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    building_elements = models.ManyToManyField("BuildingElement", on_delete=models.CASCADE)

class BuildingElement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    name = models.CharField(max_length=100)
    description = models.CharField()
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    zones = models.ManyToManyField(Zone)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class ProgressState(models.TextChoices):
        READYFORCONSTRUCTION = "RE", _("Ready for Construction")
        UNDERCONSTRUCTION = "UC", _("Under Construction")
        COMPLETED = "CO", _("Completed")
        DELAYED = "DE", _("Delayed")
        PLANNED = "PL", _("Planned")

    current_state = models.CharField(choices=ProgressState)
    class Meta:
        abstract = True

class Column(BuildingElement):
    class GeometryType:
        CIRCULAR = "C"
        SQUARE = "SQ"
        RECTENGULAR = "RE"
    
    geometry = models.CharField(choices=GeometryType)

class Wall(BuildingElement):
    color = models.CharField()
