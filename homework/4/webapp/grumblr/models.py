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

    def check_follow_or_not(self, other_user):
        if other_user.userprofile.friends.filter(email=self.user.userprofile.get_email()).exists():
            self.follow_or_not = 1
        elif other_user.userprofile.get_email() == self.user.userprofile.get_email():
            self.follow_or_not = -1
        else:
            self.follow_or_not = 0

    def get_username(self):
        return self.user.userprofile.get_email()

    def get_text(self):
        return self.text

    def get_time(self):
        return self.time


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    email = models.TextField(unique=True)
    firstname = models.TextField(default="")
    lastname = models.TextField(default="")
    age = models.IntegerField(default=1)
    photo = models.ImageField(upload_to="documents/%y/%m/%d", default=default_photo)
    background = models.ImageField(upload_to="documents/%y/%m/%d", default=default_background)
    gender = models.TextField(default="Unknown")
    saying = models.TextField(default="My Heart Is In The Work!")
    introduction = models.TextField(max_length=420, default="This lazy guy didn't say anything.")
    friends = models.ManyToManyField("self", symmetrical=False)

    '''
    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        self.follow_or_not = 0
    '''

    @property
    def friendlist(self):
        # Watch for large querysets: it loads everything in memory
        return list(self.friends.all())

    def follow(self, username):
        friend = UserProfile.objects.get(email=username)
        self.friends.add(friend)

    def unfollow(self, username):
        friend = UserProfile.objects.get(email=username)
        self.friends.remove(friend)

    '''
    def check_follow_or_not(self, username):
        if self.friends.filter(email=username).exists():
            self.follow_or_not = 1
        else:
            self.follow_or_not = 0
    '''

    def get_age(self):
        return str(self.age)

    def set_age(self, age):
        self.age = age
        return

    def get_name(self):
        return str(self.firstname) + " " + str(self.lastname)

    def get_firstname(self):
        return self.firstname

    def set_firstname(self,firstname):
        self.firstname = firstname
        return

    def get_lastname(self):
        return self.lastname

    def set_lastname(self,lastname):
        self.lastname = lastname
        return

    def get_email(self):
        return self.email

    def get_photo(self):
        return settings.MEDIA_URL + str(self.photo)

    def set_photo(self, photo):
        self.photo = photo

    def get_background(self):
        return settings.MEDIA_URL + str(self.background)

    def set_background(self, background):
        self.background = background

    def get_gender(self):
        return self.gender

    def get_date_joined(self):
        return self.user.date_joined.date()

    def get_saying(self):
        return self.saying

    def set_saying(self, saying):
        self.saying = saying
        return

    def get_introduction(self):
        return self.introduction

    def set_introduction(self, introduction):
        self.introduction = introduction
        return

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

    def check_follow_or_not(self, other_user):
        if other_user.userprofile.friends.filter(email=self.get_email()).exists():
            self.follow_or_not = 1
        else:
            self.follow_or_not = 0