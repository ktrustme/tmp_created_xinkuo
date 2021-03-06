from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'sio.views.home'),
    url(r'^home$', 'sio.views.home'),
    url(r'^create-student$', 'sio.views.create_student'),
    url(r'^create-course$', 'sio.views.create_course'),
    url(r'^register-student$', 'sio.views.register_student'),
    url(r'^get-sample-student', 'sio.views.get_sample_student'),
    url(r'^get-all-courses$', 'sio.views.get_all_courses'),
    url(r'^get-all-courses2$', 'sio.views.get_all_courses2'),
)
