from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Floor, Zone, Wall, Column
from .forms import NewFloorsForm, NewZonesForm, NewWallForm, NewColumnForm

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


def getWalls(request):
    walls = Wall.objects.all()
    context={
        'walls': walls,
    }
    return render(request, "buildingelements.html", context)

def getColumns(request):
    columns = Column.objects.all()
    context={
        'columns': columns,
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
            floor.storey = form.cleaned_data['storey']
            floor.save()

            return redirect('floors')

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
            zone.floor = form.cleaned_data['floor']
            zone.save()

  

            return redirect('zones')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewZonesForm()

    return render(request, 'newzone.html', {'form': form})

def createNewWall(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewWallForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            

            wall = Wall()
            wall.height = form.cleaned_data['height']
            wall.width = form.cleaned_data['width']  
            wall.length = form.cleaned_data['length']
            wall.description = form.cleaned_data['description']
            wall.name = form.cleaned_data['name']
            wall.personResponsible = form.cleaned_data['personResponsible']
            wall.start_date = form.cleaned_data["start_date"]
            wall.end_date = form.cleaned_data['end_date']
            wall.current_state = form.cleaned_data['progressState']
            wall.save()

            zones = form.cleaned_data.get('zones')
            if zones:
                wall.zones.set(zones)
                
            return redirect('walls')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewWallForm()

    return render(request, 'newwall.html', {'form': form})

def createNewColumn(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewColumnForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            

            column = Column()
            column.height = form.cleaned_data['height']
            column.width = form.cleaned_data['width']  
            column.length = form.cleaned_data['length']
            column.description = form.cleaned_data['description']
            column.name = form.cleaned_data['name']
            column.personResponsible = form.cleaned_data['personResponsible']
            column.start_date = form.cleaned_data["start_date"]
            column.end_date = form.cleaned_data['end_date']
            column.current_state = form.cleaned_data['progressState']
            column.save()

            zones = form.cleaned_data.get('zones')
            if zones:
                column.zones.set(zones)
                
            return redirect('columns')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewColumnForm()

    return render(request, 'newcolumn.html', {'form': form})