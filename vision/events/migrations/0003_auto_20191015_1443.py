# Generated by Django 2.2.6 on 2019-10-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20191015_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
    ]
