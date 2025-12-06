from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Floor, Zone, Wall, Column

class NewFloorsForm(forms.Form):
    storey = forms.IntegerField(label='Storey Number')


class NewZonesForm(forms.Form):
    length = forms.DecimalField(max_digits=8, decimal_places=2)
    width = forms.DecimalField(max_digits=8, decimal_places=2)
    x = forms.DecimalField(max_digits=8, decimal_places=2)
    y = forms.DecimalField(max_digits=8, decimal_places=2)
    floor = forms.ModelChoiceField(queryset=Floor.objects.all())



class NewWallForm(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    description = forms.CharField(label="description", max_length=200)
    height = forms.IntegerField()
    width = forms.IntegerField()
    length = forms.IntegerField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    personResponsible = forms.CharField(label="person responsible", max_length=200)
    zones = forms.ModelMultipleChoiceField(queryset=Zone.objects.all(), required = False, widget=forms.CheckboxSelectMultiple)
    progressState = forms.ChoiceField(choices=Wall.ProgressState.choices)
    color = forms.CharField(label="color", max_length=100)
    
class NewColumnForm(forms.Form):
    name = forms.CharField(label="name", max_length=200)
    description = forms.CharField(label="description", max_length=200)
    height = forms.IntegerField()
    width = forms.IntegerField()
    length = forms.IntegerField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    personResponsible = forms.CharField(label="person responsible", max_length=200)
    zones = forms.ModelMultipleChoiceField(queryset=Zone.objects.all(), required = False, widget=forms.CheckboxSelectMultiple)
    progressState = forms.ChoiceField(choices=Column.ProgressState.choices)
    geomerty = forms.ChoiceField(choices=Column.GeometryType.choices)
    