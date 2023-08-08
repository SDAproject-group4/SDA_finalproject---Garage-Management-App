# Generated by Django 4.2.4 on 2023-08-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0009_rename_vin_repairs_car_car_manufacturer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairs',
            name='status',
            field=models.CharField(choices=[('New', 'NOWE'), ('Pending', 'W trakcie'), ('End', 'Zakonczone')], default='New', max_length=100),
        ),
    ]