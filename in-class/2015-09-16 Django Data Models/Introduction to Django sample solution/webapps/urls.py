from django.conf.urls import include, url

urlpatterns = [
    url(r'^sio/', include('sio.urls')),
    url(r'^$', 'sio.views.home'),
]
