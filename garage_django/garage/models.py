from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=20, null=True)
    model= models.CharField(max_length=100, null=True)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=30, null=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    id = models.IntegerField
    manufacturer = models.CharField(max_length=20, null=True)
    model= models.CharField(max_length=100, null=True)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True, null=True)
    description = models.TextField(blank=True, max_length=200)

    def __str__(self):
        return f"{self.manufacturer} {self.model}, vin:{self.vin}"



class Repairs(models.Model):

    STATUS =[
        ('New', 'Nowe'),
        ('Pending', 'W trakcie'),
        ('End', 'Zakończone'),
    ]
    main_fault = models.CharField(max_length=100)
    description = models.CharField(max_length=400, default="Brak opisu.")
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, null=True)
    serv_mechanic = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.AutoField(primary_key=True)


    pick_up_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=15,
        choices=STATUS, 
        default="New"
                            )

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.main_fault
    
