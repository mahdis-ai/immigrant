from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import ProfileForm,UserForm,AuthenticationForm
from django.contrib.auth import login , authenticate
from django.contrib import messages
from .models import CustomUser
#from django.contrib.auth.forms import AuthenticationForm 
from reservation.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.http import JsonResponse ,HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import \
    require_POST, \
    require_GET
import time
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
def front(request):
    context = {
        }

    return render(request, "index.html", context)
def get_user(model_user,username):
	try:
		model_user.objects.get(username=username)
		return True
	except Exception:
		return False
@api_view(['GET'])
def homepage(request):
	if request.method == "GET":
		print("welcome")
		return Response(status.HTTP_200_OK)
@api_view(['GET','POST'])
def register_request(request):
	if request.method == "POST":
		username=request.data['name']
		password=request.data['pass']
		mobile=request.data['mobile']
		visatype=request.data['visatype']
		position=request.data['position']
		if username is not None and password is not None and mobile is not None and position is not None:
			user=User.objects.create(username=username, password=password)
	
			if(position=='lawyer'):
				Lawyer.objects.create(username=username, password=password, phone=mobile,secretary_id=1)
			if(position=='applicant'):
				if(visatype is not None):
					Applicant.objects.create(username=username, password=password, phone=mobile,visa_type=visatype)
			if(position=='secretary'):
				Secretary.objects.create(username=username, password=password, phone=mobile)
			login(request, user)
			return JsonResponse({"status":"success"})
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	return HttpResponseRedirect('/register') 
							# Create your views here.
@api_view(['POST'])
def login_request(request):
	if request.method == "POST":
		username1 = request.data['name']
		password1 = request.data['password']
	
		if username1 is not None and password1 is not None:
			try:
				check_user=User.objects.get(username=username1, password=password1)
			except User.DoesNotExist:
				print("user does not exist")
			#user = authenticate(request,username=username1, password=password1)
			if check_user is not None:
				login(request, check_user)
				user_iden2=Lawyer.objects.get(username=username1)
				if (get_user(Applicant,username1)):
					member = "applicant"
					print(member,"success")
					return JsonResponse({"status":"success","member":member})
				if(get_user(Lawyer,username1)):
					
					member ="lawyer"
					print(member,"success")
					return  JsonResponse({"status":"success","member":member})
				if(get_user(Secretary,username1)):
					member="secretary"
					print(member,"success")
					return  JsonResponse({"status":"success","member":member})
					
					#messages.info(request, f"You are now logged in as {username1}.")
					#return redirect(member,"/accounts/homepage")
			else:
				print("Invalid username or password.")
		else:
			print("Invalid !!!!!!")	
	return HttpResponseRedirect('/login')

	