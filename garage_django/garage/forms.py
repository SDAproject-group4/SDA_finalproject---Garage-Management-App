from django.forms import ModelForm
from .models import Repairs

class RepairForm(ModelForm):
    class Meta:
        model = Repairs
        fields = '__all__'