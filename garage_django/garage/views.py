from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Repairs, Car
from .forms import RepairForm, carForm
# import requests




# Create your views here.

def loginPage(request):
    page = 'login'
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
           messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User OR password does not exist')         
    
    context = {'page': page}
    return render(request, 'garage/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'garage/login_register.html', {'form': form})

def home(request):
    repairs = Repairs.objects.all()
    cars = Car.objects.all()
    active_repairs= Repairs.objects.filter(status__in=['New', 'Pending'])
    activeRepairsCount = Repairs.objects.filter(status__in=['New', 'Pending']).count()
    closedRepairsCount = Repairs.objects.filter(status__in=['End']).count()

    context = {
        'repairs':repairs, 
        'cars':cars, 
        'active_repairs':active_repairs, 
        'activeRepairsCount':activeRepairsCount,
        'closedRepairsCount':closedRepairsCount
        }
    return render(request, 'garage/home.html', context)

def repair(request, pk):
    repair = Repairs.objects.get(id=pk)
    context = {'repair':repair}
    return render(request, 'garage/repair.html', context)

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

def activeRepairByCar(request, pk):
    car = Car.objects.get(id=pk)
    active_repairs = Repairs.objects.get().filter(id=car.id)

    context = {
        'car':car, 
        'active_repairs':active_repairs
        }
    return render(request, 'garage/active_repairs.html', context)

def repairstatus(request, pk):
    repair = Repairs.objects.get(id=pk)
    context = {'repair':repair}
    return render(request, "garage/repair_status.html", context)
