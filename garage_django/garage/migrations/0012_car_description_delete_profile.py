# Generated by Django 4.2.4 on 2023-08-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0011_alter_repairs_status_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
