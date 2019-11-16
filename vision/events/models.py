from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from datetime import datetime


# Learn to manipulate models here https://docs.djangoproject.com/en/2.2/intro/tutorial02/

# class Event(models.Model):
#     event_name = models.CharField(max_length=50, null=False)
#     datetime_event = models.DateTimeField('Event Date - Please Format YYYY-MM-DD HH:MM', null=False)
#     date_published = models.DateTimeField(default = timezone.now)
#     description = models.TextField(null=False, verbose_name='Description')
#     location = models.CharField(max_length=100, null=False)
#     author = models.ForeignKey(User, on_delete = models.CASCADE)
#     image = models.ImageField(default='RGU.jpg', upload_to='profile_pics')

class Event(models.Model):
    event_name = models.CharField(max_length=50, null=False)
    start_date = models.DateField('Event starts', blank=False, default = timezone.now)
    start_time = models.TimeField('Time', blank=False, default = timezone.now)
    end_date = models.DateField('Event ends', blank=False, default = timezone.now)
    end_time = models.TimeField('Ends at', blank=False, default = timezone.now)
    date_published = models.DateTimeField(default = timezone.now)
    description = models.TextField(null=False, verbose_name='Description')
    location = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(default='RGU.jpg', upload_to='event_pics')

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk':self.pk})

    def save(self, **kwargs):
        super().save(**kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)