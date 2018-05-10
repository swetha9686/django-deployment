from django.db import models
from django.contrib.auth.models import User


class UserExtendedModel(models.Model):
	GENDER_CHOICES = (
   					   ('M', 'Male'),
   					   ('F', 'Female'),
					 )

	user=models.OneToOneField(User)
	gender = models.CharField(choices=GENDER_CHOICES,max_length=128)
	 	# choices=(
 #   					                       ('M', 'Male'),
 #   					                       ('F', 'Female'),
	# 				                  ),
					          
	profile_pic=models.ImageField(upload_to='profile_pics',blank=True)



	def __str__(self):
		return self.user.username

