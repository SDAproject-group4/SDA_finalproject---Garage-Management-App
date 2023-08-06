from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    id = models.IntegerField
    model= models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)


class Repairs(models.Model):
    main_fault = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    serv_mechanic = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.IntegerField
    pick_up_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100,
        choices=(
            ('New', 'NOWE'),
            ('Pending', 'W trakcie'),
            ('Zakonczone', 'Zakonczone'),
        ), default="New"
                              )

    class Meta:
        ordering = ['-updated_at']


    def __str__(self):
        return self.main_fault
    
