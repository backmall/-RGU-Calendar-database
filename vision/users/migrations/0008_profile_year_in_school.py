# Generated by Django 2.2.6 on 2019-10-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_profile_year_in_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='year_in_school',
            field=models.CharField(choices=[('U1', 'Undergraduate - Year 1'), ('U3', 'Undergraduate - Year 2'), ('U3', 'Undergraduate - Year 3'), ('U4', 'Undergraduate - Year 4'), ('PG', 'Postgraduate'), ('VN', 'Volunteer')], default='U1', max_length=2),
        ),
    ]
