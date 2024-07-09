from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User_Table
from django import forms
from AppTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,"help_page.html")

def users(request):
    user_list = User_Table.objects.order_by('first_name')
    user_dict = {'users_info': user_list}
    return render(request, "users.html", context= user_dict)

def form_name(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'form_page.html', {'form': form})


