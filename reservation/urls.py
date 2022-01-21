from django.urls import path
from . import views
urlpatterns =[
    path('reservation/',views.lawyer_list),
    path('sendingdocs/',views.list,name="list")
]