import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## FAKE POP SCRIPT

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Game']


def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new webpage entry
        web_page = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        # create fake access record for that page

        access_record = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)[0]


if __name__=='__main__':
    print('Populating Scripts !')
    populate(20)
    print('populating complete')


