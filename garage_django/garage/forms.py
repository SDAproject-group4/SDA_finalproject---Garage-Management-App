from django.forms import ModelForm

from .models import Repairs, Car, Client
from django import forms
from django.shortcuts import render


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
            
class clientForm(ModelForm):
    # manufacturer = forms.CharField(max_length=20, label='Producent')
    # model = forms.CharField(max_length=20, label='Model')
    # year = forms.CharField(max_length=20, label='Rok')
    # vin = forms.CharField(max_length=20, label='VIN')
    class Meta:
            model = Client
            fields = '__all__'

class repairStatusForm(ModelForm):

    template_name = 'garage/repair_status.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        license_plate = request.POST.get('license_plate')
        phone = request.POST.get('phone')

        repair = Repairs.objects.filter(car__license_plate=license_plate, client__phone=phone).first()

        return render(request, self.template_name, {'repair': repair})