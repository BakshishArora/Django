from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": webpages_list}
    my_dict ={'title': 'This is html using Jinja and Django', 'insert_me': {1: "Bakshish", 2: "Taran", 3: "Papa", 4: "Mumma"}}
    return render(request, 'first_app/index.html', context=date_dict)