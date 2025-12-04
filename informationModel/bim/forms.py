from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Floor, Zone, BuildingElement

class NewFloorsForm(forms.Form):
    storey = forms.IntegerField(label='Storey Number')


class NewZonesForm(forms.Form):
    length = forms.DecimalField(max_digits=8, decimal_places=2)
    width = forms.DecimalField(max_digits=8, decimal_places=2)
    x = forms.DecimalField(max_digits=8, decimal_places=2)
    y = forms.DecimalField(max_digits=8, decimal_places=2)
    building_elements = forms.ModelMultipleChoiceField(queryset=BuildingElement.objects.all(), required = False)
    floor = forms.ModelChoiceField(queryset=Floor.objects.all())

class NewBuildingElementsForm(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    description = forms.CharField(label="description", max_length=200)
    height = forms.IntegerField()
    width = forms.IntegerField()
    length = forms.IntegerField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    personResponsible = forms.CharField(label="person responsible", max_length=200)
    zones = forms.ModelMultipleChoiceField(queryset=Zone.objects.all(), required = False)