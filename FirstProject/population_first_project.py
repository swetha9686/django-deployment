import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','FirstProject.settings')

import django
django.setup()


#fake population script
import random
from Firstapp.models import User
from faker import Faker

fakegen=Faker()

def add_users(n):

	for i in range(n):
		fake_fname=fakegen.first_name()
		fake_lname=fakegen.last_name()
		fake_email=fakegen.company_email()

		user_data=User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)

if __name__ == '__main__':
	add_users(10)