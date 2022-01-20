from django.urls import path
from . import views
urlpatterns =[
    path('lawyers/<int:id>/',views.applicant_list)
]