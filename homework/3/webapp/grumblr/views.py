import time
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from grumblr.models import *
from django.core.exceptions import *

# Create your views here.


@login_required
def home(request):
    context={}
    errors = []
    context['errors'] = errors
    grumbles = []

    if request.method == 'GET':
        grumbles = grumble.objects.all()
        grumbles.reverse()
        context['grumbles'] = grumbles
        profile = request.user.userprofile
        context['profile'] = profile
        return render(request, 'grumblr/global_post.html', context)

    if request.method == 'POST':
        text = request.POST['grumble_text']
        if len(text) == 0 or len(str(text).split()) > 45:
            errors.append("Invalid grumble length...")
        else:
            new_grumble = grumble(text=text, user=request.user)
            new_grumble.save()

        profile = request.user.userprofile
        context['profile'] = profile
        grumbles = grumble.objects.all()
        grumbles.reverse()
        context['grumbles'] = grumbles
        return render(request, 'grumblr/global_post.html', context)


def signup(request):
    context = {}
    if request.method =="GET":
        return render(request, 'grumblr/signup.html')
    pass

    errors=[]
    context['errors'] = errors

    #A bunch of ... validation...

    if not 'username' in request.POST or not request.POST['username']:
        errors.append('Email Address Required.')
    else:
        context['username'] = request.POST['username']

    if not 'firstname' in request.POST or not request.POST['firstname']:
        errors.append('First Name Required.')
    else:
        context['firstname'] = request.POST['firstname']

    if not 'lastname' in request.POST or not request.POST['lastname']:
        errors.append('Last Name Required.')
    else:
        context['lastname'] = request.POST['lastname']

    if not 'password1' in request.POST or not request.POST['password1']:
        errors.append('Password Required.')
    if not 'password2' in request.POST or not request.POST['password2']:
        errors.append('Password Confirm Required.')

    if 'password1' in request.POST and 'password2' in request.POST \
        and request.POST['password1'] and request.POST['password2'] \
        and request.POST['password1'] != request.POST['password2']:
        errors.append('Password Mismatch!')

    if len(User.objects.filter(username = request.POST['username'])) > 0:
        errors.append('Email Already Registered. Change another one')

    if errors:
        context['errors'] = errors
        return render(request, 'grumblr/signup.html', context)

    new_user = User.objects.create_user(username=request.POST['username'],\
                                        password=request.POST['password1'])
    new_user.save()

    new_user_profile = UserProfile.objects.create(
        user=new_user,
        firstname=request.POST['firstname'],
        lastname=request.POST['lastname'],
        email=request.POST['username'])
    new_user_profile.set_rand_photo()
    new_user_profile.set_rand_saying()
    new_user_profile.set_rand_background()
    new_user_profile.save()

    new_user = authenticate(username=request.POST['username'],\
                            password=request.POST['password1'])
    login(request,new_user)
    return redirect('/home')


@login_required
def profile(request, username=""):

    context = {}
    errors = []
    context['errors'] = errors
    if request.method == "GET":
        if len(username) == 0:
            user = request.user
        else:
            user = User.objects.get(username=username)

        grumbles = grumble.objects.filter(user=user)
        context['grumbles'] = grumbles
        context['user'] = request.user
        profile = user.userprofile
        context['profile'] = profile

        return render(request, 'grumblr/profile.html', context)

    return render(request, 'grumblr/profile.html', context)

