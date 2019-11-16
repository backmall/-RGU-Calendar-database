# Generated by Django 2.2.6 on 2019-11-16 19:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20191116_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Event Ends'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Ends at'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Event Begins'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Begins at'),
        ),
    ]
