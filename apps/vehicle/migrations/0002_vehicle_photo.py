# Generated by Django 2.1 on 2018-09-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='photo',
            field=models.ImageField(default='photos_cars/photo_car_default.jpg', upload_to='photos_cars/%d'),
        ),
    ]