"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    url(r'^$', 'grumblr.views.home'),
    url(r'^home', 'grumblr.views.home'),
    url(r'^login', 'django.contrib.auth.views.login',{'template_name':'grumblr/login.html'}),
    url(r'^signup', 'grumblr.views.signup'),
    url(r'^profile$', 'grumblr.views.profile'),
    url(r'^follow_(?P<username>.*)$', 'grumblr.views.follow'),
    url(r'^unfollow_(?P<username>.*)$', 'grumblr.views.unfollow'),
    url(r'^following_post_page$', 'grumblr.views.following_post_page'),
    url(r'^profile/(?P<username>.*)$', 'grumblr.views.profile'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
            'grumblr.views.reset_confirm', name='password_reset_confirm'),
    url(r'^password_reset/$', 'grumblr.views.reset', name='password_reset'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
