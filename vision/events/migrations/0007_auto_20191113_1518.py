# Generated by Django 2.2.6 on 2019-11-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20191113_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='RGU.jpg', upload_to='../media/event_pics'),
        ),
    ]
