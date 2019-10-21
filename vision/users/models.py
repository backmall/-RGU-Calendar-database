from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserObj(object):
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def __str__(self):
		return '%s (%s)' % (self.username, self.email)