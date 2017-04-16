from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View 
from .forms import UserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	return render(request,'loginapp/index.html')

@login_required
def home(request):
	return HttpResponse("You are HomePage.")

class signup(View):
	form_class=UserForm
	template_name='loginapp/signup.html'

	#display a blank form
	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	#process form data
	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():

			user=form.save(commit=False)

			#cleaned data
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return render (request,'loginapp/logged.html')


		return render(request,self.template_name,{'form':form})

def signin(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)

		if user is not None:
			if user.is_active:
				login(request,user)
				return render(request,'loginapp/logged.html',{'user':request.user})
			else:
				return render(request,'loginapp/signin.html',{'error_message':'Inactive User'})
		else:
			return render (request,'loginapp/signin.html',{'error_message':'Incorrect Username or Password'})

	return render(request,'loginapp/signin.html')


def logged(request):
	if not request.user.is_authenticated():
		form=UserForm()
		return render(request,'loginapp/signup.html',{'form':form,'error_message':'You are not Authenticated'})
	else:
		return render(request,'loginapp/logged.html',{'user':request.user})

def logout_user(request):
	logout(request)
	form=UserForm(request.POST or None)
	return render(request,'loginapp/signin.html',{'form':form})




