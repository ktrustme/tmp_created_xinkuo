import time
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from models import *
from django.core.exceptions import *
from django.http import HttpResponse
from forms import *
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

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
        for one_grumble in grumbles:
            one_grumble.check_follow_or_not(request.user)
        context['grumbles'] = grumbles
        profile = request.user.userprofile
        context['profile'] = profile

        return render(request, 'grumblr/global_post_page.html', context)

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
        for one_grumble in grumbles:
            one_grumble.check_follow_or_not(request.user)
        grumbles.reverse()
        context['grumbles'] = grumbles
        return render(request, 'grumblr/global_post_page.html', context)


@login_required
def following_post_page(request):
    context={}
    errors = []
    context['errors'] = errors
    grumbles = []

    friend_list = []
    for friend in request.user.userprofile.friendlist:
        friend_list.append(friend.user)
    if request.method == 'GET':
        grumbles = grumble.objects.filter(user__in=friend_list)
        grumbles.reverse()
        for one_grumble in grumbles:
            one_grumble.check_follow_or_not(request.user)
        context['grumbles'] = grumbles
        profile = request.user.userprofile
        context['profile'] = profile
        return render(request, 'grumblr/following_post_page.html', context)

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
        for one_grumble in grumbles:
            one_grumble.check_follow_or_not(request.user)
        grumbles.reverse()
        context['grumbles'] = grumbles
        return render(request, 'grumblr/following_post_page.html', context)



def signup(request):
    context = {}
    if request.method =="GET":
        context['form'] = RegistrationForm()
        return render(request, 'grumblr/signup.html', context)
    pass

    errors=[]
    context['errors'] = errors

    form = RegistrationForm(request.POST)
    context['form'] = form
    if not form.is_valid():
        return render(request, 'grumblr/signup.html', context)

    new_user = User.objects.create_user(username=form.cleaned_data['email'],
                                        email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password1'])
    new_user.save()

    new_user_profile = UserProfile.objects.create(
        user=new_user,
        firstname=form.cleaned_data['firstname'],
        lastname=form.cleaned_data['lastname'],
        email=form.cleaned_data['email'])

    new_user_profile.set_rand_photo()
    new_user_profile.set_rand_saying()
    new_user_profile.set_rand_background()
    new_user_profile.save()
    new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
    login(request, new_user)
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
        user_profile = user.userprofile
        user_profile.check_follow_or_not(request.user)
        context['profile'] = user_profile
        edit_form = EditProfileForm()

        edit_form.fields['firstname'].initial = user_profile.get_firstname()
        edit_form.fields['lastname'].initial = user_profile.get_lastname()
        edit_form.fields['age'].initial = user_profile.get_age()
        edit_form.fields['saying'].initial = user_profile.get_saying()
        edit_form.fields['introduction'].initial = user_profile.get_introduction()

        context['form'] = edit_form

        if username and username != request.user.username:
            return render(request, 'grumblr/profile_guest_view.html', context)
        else:
            return render(request, 'grumblr/profile.html', context)

    if request.method == "POST":
        if username:
            return redirect('/profile')

        user = request.user

        user_profile = UserProfile.objects.get(user=user)
        user_profile.check_follow_or_not(request.user)
        grumbles = grumble.objects.filter(user=user)

        edit_form = EditProfileForm(request.POST, request.FILES)


        context['form'] = edit_form
        context['grumbles'] = grumbles
        context['profile'] = user_profile
        context['user'] = request.user

        if not edit_form.is_valid():
            context["error_flag"]=1
            return render(request, 'grumblr/profile.html', context)

        user_profile.set_age(int(edit_form.cleaned_data['age']))
        user_profile.set_firstname(edit_form.cleaned_data['firstname'])
        user_profile.set_lastname(edit_form.cleaned_data['lastname'])
        user_profile.set_saying(edit_form.cleaned_data['saying'])
        user_profile.set_introduction(edit_form.cleaned_data['introduction'])
        if edit_form.cleaned_data['photo']:
            user_profile.set_photo(edit_form.cleaned_data['photo'])
        if edit_form.cleaned_data['background']:
            user_profile.set_background(edit_form.cleaned_data['background'])
        user_profile.save()

        edit_form.fields['firstname'].initial = user_profile.get_firstname()
        edit_form.fields['lastname'].initial = user_profile.get_lastname()
        edit_form.fields['age'].initial = user_profile.get_age()
        edit_form.fields['saying'].initial = user_profile.get_saying()
        edit_form.fields['introduction'].initial = user_profile.get_introduction()

        return render(request, 'grumblr/profile.html', context)

    return render(request, 'grumblr/profile.html', context)


@login_required
def edit_profile(request, username=""):
    context = {}
    return render(request, 'grumblr/profile.html', context);

@login_required
def follow(request, username=""):
    newfriend = UserProfile.objects.get(email=username)
    if newfriend:
        request.user.userprofile.follow(username)
        request.user.userprofile.save()
        return HttpResponse("success")
    else:
        return HttpResponse("fail")

@login_required
def unfollow(request, username=""):
    friend = UserProfile.objects.get(email=username)
    print("HERE")
    if friend:
        request.user.userprofile.unfollow(username)
        print("HERE2")
        return HttpResponse("success")
    print("HERE3")
    return HttpResponse("success")


def reset_password(request, username=""):
    subject = "Grumblr: Reset Password Request"
    message = "HI"
    from_email ="Do Not Reply <xkuo@grumblr.com>"
    recipient_list = ["kuokuo@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='grumblr/password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect="/login")


def reset(request):
    if(request.method=="POST"):
        print(request.POST["email"])
    return password_reset(request, template_name='grumblr/password_reset.html',
        email_template_name='grumblr/reset_email.html',
        subject_template_name='grumblr/reset_subject.txt',
        post_reset_redirect="/login")
