# Generated by Django 2.2.6 on 2019-11-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20191116_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime_event',
            field=models.DateTimeField(verbose_name='Event Date - Please Format YYYY-MM-DD HH:MM'),
        ),
    ]
