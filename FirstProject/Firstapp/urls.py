from django.conf.urls import url
from Firstapp import views

app_name='Firstapp'

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^blogpost/',views.blogpost,name='blogpost'),
	

]