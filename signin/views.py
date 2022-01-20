from django.shortcuts import render
from .models import Profile
from .forms import (LoginForm ,
                    UserRegistrationForm ,
                    )
from reservation.models import Applicant
from django.contrib.auth import authenticate ,logout ,login
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def user_login(request):


    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)

            if user:

                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('reservation'))
                else:
                    return HttpResponse('User is not Active')
            else:
                return HttpResponse('User Not Available')
    else:
        form = LoginForm()
def register(request):



    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Applicant.objects.create(user = user)
            return HttpResponseRedirect(reverse('user_login'))
    else:
        form = UserRegistrationForm()



    return render(request=request, template_name="signin/register.html", context={"register_form":form})

