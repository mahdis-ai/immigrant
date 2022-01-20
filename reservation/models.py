from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Applicant(models.Model):
    work_visa='work'
    study_visa='study'
    VISA_CHOICES=[
        (work_visa,'work'),
        (study_visa,'study'),
    ]
    username= models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    password=models.CharField(max_length=255,)
    visa_type=models.CharField(max_length=100,choices=VISA_CHOICES,default=study_visa)
    def __str__(self):
        return self.username
class Secretary(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    def __str__(self):
        return self.first_name+" "+self.last_name
class Lawyer(models.Model):  
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255) 
    reservation_schedule=models.CharField(max_length=255)
    secretary= models.ForeignKey(Secretary, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name+" "+self.last_name


class Application(models.Model):
    APPLICATION_COMPLETE='C'
    APPLICATION_REJECTED='R'
    APPLICATION_STATUS=[
        (APPLICATION_COMPLETE,'COMPLETE'),
        (APPLICATION_REJECTED,'REJECTED')

    ]
    application_status = models.CharField(max_length=1,choices=APPLICATION_STATUS,default=APPLICATION_COMPLETE)
    placed_at= models.DateTimeField(auto_now_add=True)
    applicant=models.OneToOneField(Applicant,on_delete=models.CASCADE,primary_key=True)
    lawyer=models.ForeignKey(
        Lawyer,on_delete=models.CASCADE)
    secretary=models.ForeignKey(Secretary, on_delete=models.CASCADE)
    def __str__(self):
        return self.application_status





    
    