from django.shortcuts import render
from .models import Repairs


# repairs = [
#     {'id':1, 'name':'Uszkodzone drzwi'},
#     {'id':2, 'name':'Naprawa silnika'},
#     {'id':3, 'name':'Dziurawy tłumik'},
# ]

# Create your views here.
def home(request):
    repairs = Repairs.objects.all()
    return render(request, 'garage/home.html', {'repairs':repairs})

def login(request):
    return render(request, 'login.html')

def repair(request, pk):
    repair = Repairs.objects.get(id=pk)
    context = {'repair':repair}
    return render(request, 'garage/repair.html', context)