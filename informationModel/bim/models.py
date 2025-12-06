import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Floor(models.Model):
    globalId = models.UUIDField(default=uuid.uuid4, editable = False, unique=True)
    storey = models.IntegerField()
    
class Zone(models.Model):
    globalId = models.UUIDField(default=uuid.uuid4, editable = False, unique=True)
    length = models.DecimalField(max_digits=8, decimal_places=2)
    width = models.DecimalField(max_digits=8,decimal_places=2)
    x = models.DecimalField(max_digits=8, decimal_places=2)
    y = models.DecimalField(max_digits=8, decimal_places=2)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    walls = models.ManyToManyField("Wall")
    columns = models.ManyToManyField("Column")

class BuildingElement(models.Model):
    globalId = models.UUIDField(default=uuid.uuid4, editable = False, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(default="Generic Building Element", max_length=100)
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    personResponsible = models.CharField(default="Sicco Oortwijn", max_length=100)
    zones = models.ManyToManyField(Zone)

    class ProgressState(models.TextChoices):
        READYFORCONSTRUCTION = "RE", _("Ready for Construction")
        UNDERCONSTRUCTION = "UC", _("Under Construction")
        COMPLETED = "CO", _("Completed")
        DELAYED = "DE", _("Delayed")
        PLANNED = "PL", _("Planned")

    current_state = models.CharField(choices=ProgressState, default=ProgressState.PLANNED)

    class Meta:
        abstract = True

class Column(BuildingElement):
    class GeometryType(models.TextChoices):
        CIRCULAR = "C"
        SQUARE = "SQ"
        RECTENGULAR = "RE"
    
    geometry = models.CharField(choices=GeometryType)

class Wall(BuildingElement):
    color = models.CharField()
