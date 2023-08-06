from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    id = models.IntegerField
    manufacturer = models.CharField(max_length=20, null=True)
    model= models.CharField(max_length=100, null=True)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True, null=True)
    description = models.TextField(blank=True, max_length=200)

    def __str__(self):
        return f"{self.manufacturer} {self.model}, vin:{self.vin}"


class Repairs(models.Model):

    STATUS_NAMES =[
        ('New', 'Nowe'),
        ('Pending', 'W trakcie'),
        ('End', 'Zakończone'),
    ]
    main_fault = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, null=True)
    serv_mechanic = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.IntegerField
    pick_up_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=15,
        choices=STATUS_NAMES, 
        default="New"
                            )

    class Meta:
        ordering = ['-updated_at']


    def __str__(self):
        return self.main_fault
    
