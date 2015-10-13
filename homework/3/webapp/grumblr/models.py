from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
import random
import os
# Create your models here.

default_photo = "/default_photo/sillydog.jpg"
default_photo_dir = os.path.join(settings.MEDIA_ROOT,"default_photo")

default_background = "/default_background/beach.jpg"
default_background_dir = os.path.join(settings.MEDIA_ROOT,"default_background")

saying_list = ["My Heart Is In The Work!",
               "Rose Is Red, Violet Is Blue~",
               "It was the best of times, it was the worest of times...",
               "I Like Grumble!",
               "One apple a day, keeps doctor away."]
class grumble(models.Model):
    text = models.CharField(max_length=45)
    time = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User)


    def get_name(self):
        return self.user.userprofile.get_name()

    def get_username(self):
        return self.user.userprofile.get_email()
    def get_text(self):
        return self.text

    def get_time(self):
        return self.time


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    firstname = models.TextField(default="")
    lastname = models.TextField(default="")
    photo = models.ImageField(upload_to="documents/%y/%m/%d", default=default_photo)
    background = models.ImageField(upload_to="documents/%y/%m/%d", default=default_background)
    email = models.TextField()
    gender = models.TextField(default="Unknown")
    saying = models.TextField(default="My Heart Is In The Work!")

    def get_name(self):
        return str(self.firstname) + " " + str(self.lastname)

    def get_email(self):
        return self.email

    def get_photo(self):
        return settings.MEDIA_URL + str(self.photo)


    def get_background(self):
        return settings.MEDIA_URL + str(self.background)

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.user.date_joined.date()

    def get_saying(self):
        return self.saying

    def set_rand_saying(self):
        pos = random.randint(0, len(saying_list)-1)
        self.saying = saying_list[pos]

    def set_rand_photo(self):
        photos = [photo for photo in os.listdir(default_photo_dir) if photo.endswith(".jpg")]
        pos = random.randint(0,len(photos)-1)
        self.photo = "/default_photo/" + photos[pos]

    def set_rand_background(self):
        bgs = [bg for bg in os.listdir(default_background_dir) if (bg.endswith(".jpg") or bg.endswith(".jpeg"))]
        pos = random.randint(0,len(bgs)-1)
        self.background = "/default_background/" + bgs[pos]