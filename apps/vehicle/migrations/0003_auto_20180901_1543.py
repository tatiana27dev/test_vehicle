# Generated by Django 2.1 on 2018-09-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_vehicle_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]