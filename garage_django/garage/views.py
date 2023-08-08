from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Repairs
from .forms import RepairForm


# repairs = [
#     {'id':1, 'name':'Uszkodzone drzwi'},
#     {'id':2, 'name':'Naprawa silnika'},
#     {'id':3, 'name':'Dziurawy tłumik'},
# ]

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
    return render(request, 'garage/home.html', {'repairs':repairs})

def repair(request, pk):
    repair = Repairs.objects.get(id=pk)
    context = {'repair':repair}
    return render(request, 'garage/repair.html', context)

def createRepair(request):
    form = RepairForm()
    if request.method == 'POST':
        print(request.POST)
    context = {'form': form}
    return render(request, 'garage/create_repair.html', context)