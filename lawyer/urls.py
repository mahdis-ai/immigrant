from django.urls import path
from . import views
urlpatterns =[
    path('lawyers/',views.applicant_list)
]