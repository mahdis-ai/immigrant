from django.contrib import admin
from . import models
admin.site.register(models.Applicant)
admin.site.register(models.Lawyer)
admin.site.register(models.Secretary)
admin.site.register(models.Application)
# Register your models here.
