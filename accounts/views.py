from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from django.contrib.auth.models import User
 
def show_profile(request):
    return render(request, "profile.html")


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
          
            user_avatar = models.ImageField(upload_to='media/avatars/') 
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')
            user = user_form.save()
          
            profile.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            HttpResponseRedirect('profile.html')
            # was able to get a user to succesfullly create a profile by ommitting the return above
            # the return above was ending the loop too early - making profile unable to create
   
    user_form = SignUpForm()
    profile_form = ProfileForm()
    return render(request, 'registration/signup.html',  
            { 
                'user_form': user_form, 
                'profile_form': profile_form
            })



def create_profile(sender, **kw):
    user = kw["instance"]
    if kw["created"]:
        profile = Profile()
        profile.user = user
        profile.save()

post_save.connect(create_profile, sender=User)