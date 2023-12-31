# Generated by Django 4.2.4 on 2023-08-06 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0007_repairs_vin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
        migrations.RemoveField(
            model_name='repairs',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='vin',
            field=models.CharField(max_length=17, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='repairs',
            name='vin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='garage.car'),
        ),
    ]
