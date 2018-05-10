from django import forms
from django.contrib.auth.models import User
from Firstapp.models import UserExtendedModel

class User_Form(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','size':'44','class':'form-control'}))
	first_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','class':'form-control'}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','class':'form-control'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail','size':'44','class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'password','size':'44','class':'form-control'}))
	class Meta():
		model=User
		exclude=['groups','user_permissions']
		fields=['username','first_name','last_name','email','password']

class UserExtendedModel_Form(forms.ModelForm):
	GENDER_CHOICES = (
   					   ('M', 'Male'),
   					   ('F', 'Female'),
					 )
	gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
	class Meta():
		model=UserExtendedModel
		fields=['gender','profile_pic']



# class Login_Form(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput)
# 	class Meta():
# 		model=Login_model
# 		fields=['username','password']