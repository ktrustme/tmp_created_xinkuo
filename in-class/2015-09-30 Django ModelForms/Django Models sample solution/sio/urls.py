from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'sio.views.home'),
    url(r'^home$', 'sio.views.home'),
    url(r'^create-student$', 'sio.views.create_student'),
    url(r'^create-course$', 'sio.views.create_course'),
    url(r'^register-student$', 'sio.views.register_student'),
]
