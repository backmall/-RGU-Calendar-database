# Generated by Django 2.2.6 on 2019-11-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20191114_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='RGU.jpg', upload_to='event_pics'),
        ),
    ]
