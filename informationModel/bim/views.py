from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Floor, Zone, BuildingElement, Wall, Column
# from .forms import Course, Student

def index(request):
    return HttpResponse("Hello, world. You're at the students index.")

def getFloors(request):
    floors = Floor.objects.all()
    context={
        'floors': floors,
    }
    return render(request, "floors.html", context)

def getZones(request):
    zones = Zone.objects.all()
    context={
        'zones': zones,
    }
    return render(request, "zones.html", context)


def getBuildingElements(request):
    buildingElements = BuildingElement.objects.all()
    context={
        'buildingElements': buildingElements,
    }
    return render(request, "buildingelements.html", context)

