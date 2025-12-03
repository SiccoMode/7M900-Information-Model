from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewFloorsForm(forms.Form):
    storey = forms.CharField(label='Storey Number', max_length=200)
    teacher = forms.CharField(label='Teacher name', max_length=200)


class NewZonesForm(forms.Form):
    length = forms.CharField(label='Course name', max_length=200)
    width = forms.CharField(label='Teacher name', max_length=200)
    x = forms.CharField(label='Identifier (student card number)', max_length=20)
    y = forms.CharField(label= "y_coordinate", max_length=20)
    building_elements = forms.CharField(label="building_elements", max_length=20)

class NewBuildingElementsForm():
    name = forms.CharField(label="name", max_length=200)