from django.shortcuts import render
from app_three import forms
# from http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'temp_response': "This is random respons"}
    return render(request, "index.html", context=my_dict)


def form_name(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation success")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
            # Do something code
    return render(request, 'forms_page.html', context={'form': form})