from django.conf.urls import url,include
from . import views

app_name='loginapp'

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^signin/$',views.signin,name='signin'),
	url(r'^logged/$',views.logged,name='logged'),
	url(r'^logout/$',views.logout_user,name='logout_user'),
	url(r'^signup/',views.signup.as_view(),name='signup'),
	
]