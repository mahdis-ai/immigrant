from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class Profile(models.Model):

    username= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone= models.CharField(max_length=255)
    USERNAME_FIELD = 'phone'
    def __str__(self):
        return "profile {}".format(self.user.username)
# Create your models here.
