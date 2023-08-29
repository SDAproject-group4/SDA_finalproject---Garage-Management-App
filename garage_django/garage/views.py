from django.shortcuts import render, redirect

from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Repairs, Car, Client, Messages
from .forms import RepairForm, carForm, clientForm

from django.conf import settings
from django.core.mail import send_mail


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
    return redirect('index')

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

@login_required(login_url="login/")
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
    car = Car.objects.get(id=repair.car_id)
    client = Client.objects.get(id=repair.client_id)
    repair_messages = repair.messages_set.all().order_by('-created_at')
    # client=Client.objects.get(id=client.id)

    if request.method == 'POST':
        message = Messages.objects.create(
            user=request.user,
            repair=repair,
            body=request.POST.get('body')
        )
        return redirect('repair', pk=repair.id)

    context = {'repair':repair, 
               'car':car, 
               'client':client,
               'repair_messages':repair_messages
               }
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

def repairStatus(request):
    template_name = 'garage/repair_status.html'
    
    if request.method == 'POST':
        repair_form = RepairForm(request.POST)
        if repair_form.is_valid():
            license_plate = repair_form.cleaned_data['license_plate']
            phone = repair_form.cleaned_data['phone']

            repair = Repairs.objects.filter(car__license_plate=license_plate, client__phone=phone).first()

            return render(request, template_name, {'repair_form': repair_form, 'repair': repair})

    else:
        repair_form = RepairForm()
        return render(request, template_name, {'repair_form': repair_form})


def clientLogin(request):
    
    return render(request, 'garage/client_login.html')

def index(request):
    return render(request, 'garage/index.html')

def addClient(request):
    form = clientForm()
    if request.method == 'POST':
        form = clientForm(request.POST)
        if form.is_valid():
            addclient = form.save(commit=False)
            addclient.user = request.user
            addclient.save()
        email=request.POST.get('email')
        send_mail(
            "Zostałeś dodany jako klient",
            "Twój samochód został dodany do naszego systemu", 
            'settings.EMAIL_HOST_USER',
            ['sloneczny40@gmail.com'],
            fail_silently=False
            )
        return redirect('home')

    context = {'form': form}
    return render(request, 'garage/add_client.html', context)

def cars(request):
    car = Car.objects.all()

    context = {
        'car':car, 
        }
    return render(request, 'garage/cars.html', context)