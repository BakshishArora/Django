from django.urls import path
from AppTwo import views

urlpatterns = [
    path('', views.users, name="users"),
    path('/formpage', views.form_name, name = "form_name"),
]