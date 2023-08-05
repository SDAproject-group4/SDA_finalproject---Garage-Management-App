from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class PersonMechanic(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     function = models.CharField(max_length=100, default='Mechanik')
#     id = models.IntegerField
#     avatar = models.ImageField(upload_to='images/avatars', width_field=200, height_field=200, default='images/avatars/default.png')
#     added_date = models.DateTimeField(auto_now_add=True)
    

class Repairs(models.Model):
    main_fault = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    serv_mechanic = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.IntegerField
    pick_up_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100,
        choices=(
            ('nowe', 'New'),
            ('w trakcie', 'Pending'),
            ('zakończone', 'Rejected'),
        ), default="New"
                              )

    def __str__(self):
        return self.main_fault
    
