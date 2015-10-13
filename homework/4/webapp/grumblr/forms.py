__author__ = 'kuoxin'

from django import forms
from django.contrib.auth.models import User
from models import *
import re

class RegistrationForm(forms.Form):
    email = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    firstname = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password1 = forms.CharField(max_length = 200, label = 'Password', widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length = 200, label = 'Password', widget=forms.TextInput(attrs={'placeholder': 'Re-confirm your password'}))

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        firstname = cleaned_data.get('firstname')
        lastname = cleaned_data.get('lastname')
        if not firstname:
            raise forms.ValidationError("Enter first name")

        if not lastname:
            raise forms.ValidationError("Enter last name")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match!")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username__exact=email):
            raise forms.ValidationError("Email is already registered!")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Invalid email address format!")
        return email

class EditProfileForm(forms.Form):
    #email = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    firstname = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    age = forms.IntegerField(min_value=0, max_value=150, label='Age', widget=forms.NumberInput)

    CHOICES=[('male','Male'),
         ('female','Female'),
        ('other','Other'),
        ('unknown','Unknown')]
    #gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    saying = forms.CharField(max_length=100, widget=forms.Textarea())
    introduction = forms.CharField(max_length=100, widget=forms.Textarea())
    photo = forms.ImageField(required=False)
    background = forms.ImageField(required=False)
    def clean(self):
        cleaned_data = super(EditProfileForm, self).clean()
        return cleaned_data
    '''
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username__exact=email):
            raise forms.ValidationError("Email is already registered!")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Invalid email address format!")
        return email
    '''

class LoginForm(forms.Form):
    email = forms.CharField(max_length = 100, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(max_length = 200, label = 'Password',
                               widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        return cleaned_data

