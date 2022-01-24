from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import ProfileForm,UserForm,AuthenticationForm
from django.contrib.auth import login , authenticate
from django.contrib import messages
from .models import CustomUser
#from django.contrib.auth.forms import AuthenticationForm 
from reservation.models import *
from django.contrib.auth.models import User
def get_user(model_user,username):
	try:
		model_user.objects.get(username=username)
		return True
	except Exception:
		return False
def homepage(request):
	return render(request,"home.html")
def register_request(request):
	if request.method == "POST":
		user_form=UserForm(request.POST)
		form = ProfileForm(request.POST)
		if (form.is_valid() and user_form.is_valid()):
			user= user_form.save()
			#user_profile=form.save()
			username1=user_form.cleaned_data["username"]
			password1=user_form.cleaned_data["password"]
			phone1=form.cleaned_data["phone"]
			visa_type1=form.cleaned_data["visa_type"]
			membership1=form.cleaned_data["membership"]
			if(membership1=='lawyer'):
				Lawyer.objects.create(username=username1, password=password1, phone=phone1,secretary_id=1)
			elif(membership1=='applicant'):
				if(visa_type1 is not None):
					Applicant.objects.create(username=username1, password=password1, phone=phone1,visa_type=visa_type1)
			else:
				Secretary.objects.create(username=username1, password=password1, phone=phone1)
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('/accounts/homepage')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = ProfileForm()
	user_form=UserForm()
	return render (request=request, template_name="register.html", context={"profile":user_form,"register_form":form})
							# Create your views here.
def login_request(request):
	if request.method == "POST":
		form=AuthenticationForm(request=request,data=request.POST)
		if form.is_valid():
			username1 = form.cleaned_data.get('username')
			password1= form.cleaned_data.get('password')
			check_user=User.objects.get(username=username1, password=password1)
			user = authenticate(username=username1, password=password1)
			if check_user is not None:
				login(request, user)
				user_iden2=Lawyer.objects.get(username=username1)
				if (get_user(Applicant,username1)):
					member = "applicant"
					return redirect('/reservation')
				elif(get_user(Lawyer,username1)):
					member ="lawyer"
					return redirect('/lawyer/panel')
				else:
					member="secretary"
					return redirect('/secretary')
				
				#messages.info(request, f"You are now logged in as {username1}.")
				#return redirect(member,"/accounts/homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			print("login failed")
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})