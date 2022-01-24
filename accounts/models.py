from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.contrib.auth.models import User, UserManager

class CustomUser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=50)
    membership=models.CharField(max_length=50)
    visa_type=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.user_name


