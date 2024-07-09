import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "ProTwo.settings")

import django
django.setup()
from AppTwo.models import User_Table
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email_id = fakegen.free_email()

        _user = User_Table.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, url=fake_email_id)[0]
        _user.save()


if __name__=='__main__':
    print("Populating in User Table")
    populate(20)
    print("User Populated successfully")

