from django.db import models

# Create your models here.


class Repairs(models.Model):
    main_fault = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    id = models.IntegerField
    pick_up_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # mechanik przyjmujacy zlecenie
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
    
