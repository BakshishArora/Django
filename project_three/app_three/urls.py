from django.urls import path
from project_three import views

url_patterns =[
    path('', views.index, name="index"),
]