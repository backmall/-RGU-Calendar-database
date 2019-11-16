from django.db.models.signals import post_save
from django.contrib.auth.models import User
import django
from django.dispatch import receiver
from .models import Profile

# when user is saved, send signal (post_save) and go to function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


# **kwarg accepts any keyword arguments passed
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()