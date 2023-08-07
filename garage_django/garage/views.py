from django.shortcuts import render, redirect
from .models import Repairs, Car
from .forms import RepairForm, carForm
from django.contrib.auth.models import User
import requests




def home(request):
    repairs = Repairs.objects.all()
    cars = Car.objects.all()
    context = {'repairs':repairs, 'cars':cars}
    return render(request, 'garage/home.html', context)

def repair(request, pk):
    repair = Repairs.objects.get(id=pk)
    context = {'repair':repair}
    return render(request, 'garage/repair.html', context)

# def activeRepair(request):
#     active_repairs = Repairs.objects.filter(status="New")
#     context = {'active_repairs':active_repairs}
#     return render(request, 'garage/repair.html', context)

def createRepair(request):
    form = RepairForm()
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'garage/create_repair.html', context)

def updateRepair(request, pk):
    repair = Repairs.objects.get(id=pk)
    form = RepairForm(instance=repair)
    if request.method == 'POST':
        form = RepairForm(request.POST, instance=repair)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'garage/create_repair.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    repairs = user.repair_set.all()
    context = {'user':user, 'repairs':repairs}
    return render(request, 'garage/profile.html', context)

def addCar(request):
    form = carForm()
    if request.method == 'POST':
        form = carForm(request.POST)
        if form.is_valid():
            addcar = form.save(commit=False)
            addcar.user = request.user
            addcar.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'garage/add_car.html', context)

def car(request, pk):
    car = Car.objects.get(id=pk)
    repair = Repairs.objects.get(id=pk)
    context = {'car':car, 'repair':repair}
    return render(request, 'garage/car.html', context)

def repairsCount(request):
    closed_case = Repairs.objects.filter(status="End").count()
    context = {'closed_case':closed_case}
    return render(request, 'garage/home.html', context)


