from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Firstapp.forms import User_Form,UserExtendedModel_Form


from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def index(request):
	
	registered=False
	if request.method == "POST":
		if request.POST.get('form_type') == 'formTwo':
			userform=User_Form(request.POST)
			extendedform=UserExtendedModel_Form(request.POST)

			if userform.is_valid() and extendedform.is_valid():
				user=userform.save()
				user.set_password(user.password)    #encryps the password inside the model
				user.save()

				extend=extendedform.save(commit=False)
				extend.user=user     #extend.user is the variable used in onetoone relationship in models, user is the variable we stored from user data on to
			
				if 'profile_pic' in request.FILES:
					extend.profile_pic=request.FILES['profile_pic']  #all the fields info OF HTTP post method is sent as ditionary in request.FILES


				print(request.FILES)
				extend.save()
				registered=True

		elif request.POST.get('form_type') == 'formOne':
			username=request.POST.get('username') #get('username') is the name given in iput tag for name attribute
			password=request.POST.get('password')


			user=authenticate(username=username,password=password)

			if user:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('blogpost')
				else:
					return HttpResponse("Account Not Active")
			else:
				return HttpResponse("Not right user")
			


		#else:   we can check on this on clone projects
	else:
		userform=User_Form()
		extendedform=UserExtendedModel_Form()
	
	return render(request,'index.html',{'userform':userform,'extendedform':extendedform,'registered':registered})




@login_required
def user_logout(request):
	
	logout(request)
	return HttpResponseRedirect(reverse('index'))


	

































	


def blogpost(request):
	return render(request,'blogpost.html')

# def users(request):
# 	qs=User.objects.all()
# 	qs_dict={'userdata':qs}
# 	return render(request,'users.html',context=qs_dict)
