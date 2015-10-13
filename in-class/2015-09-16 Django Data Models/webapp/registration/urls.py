from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^create_student/', include('registration.views.create_student')),
    url(r'^create_course/', include('registration.views.create_course')),
    url(r'^register_student/', include('registration.views.register_student')),
    url(r'^list_allstudent/', include('registration.views.list_allstudent')),
]
