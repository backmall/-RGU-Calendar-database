from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
# class UserObj(object):
# 	def __init__(self, username, email, password):
# 		self.username = username
# 		self.email = email
# 		self.password = password

# 	def __str__(self):
# 		return '%s (%s)' % (self.username, self.email)

class Profile(models.Model):
    YEAR1 = 'U1'
    YEAR2 = 'U2'
    YEAR3 = 'U3'
    YEAR4 = 'U4'
    POSTGRAD = 'PG'
    VOLUNTEER = 'VN'

    USER_YEAR_AT_RGU = [
        (YEAR1, 'Undergraduate - Year 1'),
        (YEAR3, 'Undergraduate - Year 2'),
        (YEAR3, 'Undergraduate - Year 3'),
        (YEAR4, 'Undergraduate - Year 4'),
        (POSTGRAD, 'Postgraduate'),
        (VOLUNTEER, 'Volunteer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    year_in_school = models.CharField(
        max_length=2,
        choices=USER_YEAR_AT_RGU,
        default=YEAR1,
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def user_year_is(self):
        return self.year_in_school
    
    def save(self, **kwargs):
        super().save(**kwargs)

        img = Image.open(self.image.path)
        if img.height > 360 or img.width > 340:
            output_size = (360, 340)
            img.thumbnail(output_size)
            img.save(self.image.path)
