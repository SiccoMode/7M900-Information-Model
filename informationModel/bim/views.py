from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Floor, Zone, BuildingElement, Wall, Column
from .forms import NewFloorsForm, NewZonesForm, NewBuildingElementsForm

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

def createNewFloor(request):    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewFloorsForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            

            floor = Floor()
            floor.zones = form.cleaned_data['zone']
            floor.teacher = form.cleaned_data['teacher']  
            floor.save()

            return redirect('courses')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewFloorsForm()

    return render(request, 'newfloor.html', {'form': form})

def createNewZone(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewZonesForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            

            zone = Zone()
            zone.length = form.cleaned_data['length']
            zone.width = form.cleaned_data['width']  
            zone.x = form.cleaned_data['x']
            zone.y = form.cleaned_data['y']
            zone.building_elements = form.cleaned_data['building_elements']
            zone.save()

            return redirect('courses')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewFloorsForm()

    return render(request, 'newzone.html', {'form': form})

def createNewBuildingElement(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewBuildingElementsForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            

            building_element = BuildingElement()
            building_element.height = form.cleaned_data['height']
            building_element.width = form.cleaned_data['width']  
            building_element.length = form.cleaned['length']
            building_element.description = form.cleaned_data['description']
            building_element.name = form.cleaned_data['name']
            building_element.person = form.cleaned_data['personResponsible']
            building_element.start_date = form.cleaned_data["start_date"]
            building_element.end_date = form.cleaned_data['end_date']
            building_element.zones = form.cleaned_data['zones']
            building_element.save()

            return redirect('courses')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewFloorsForm()

    return render(request, 'newelement.html', {'form': form})