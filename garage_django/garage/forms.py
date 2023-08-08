from django.forms import ModelForm

from .models import Repairs, Car
from django import forms


class RepairForm(ModelForm):
    class Meta:
        model = Repairs
        fields = '__all__'
        exclude = [
            'serv_mechanic'
        ]
class carForm(ModelForm):
    # manufacturer = forms.CharField(max_length=20, label='Producent')
    # model = forms.CharField(max_length=20, label='Model')
    # year = forms.CharField(max_length=20, label='Rok')
    # vin = forms.CharField(max_length=20, label='VIN')
    class Meta:
            model = Car
            fields = '__all__'